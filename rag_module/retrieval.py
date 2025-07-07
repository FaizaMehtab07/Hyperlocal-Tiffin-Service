import json
from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient

class FoodRetriever:
    def __init__(self, data_path='data/food_info.json'):
        self.data_path = data_path
        # Use PersistentClient with storage path for persistence
        self.client = PersistentClient(path="chromadb_storage")
        self.collection_name = "food_items"
        self.collection = None
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self._load_data_and_create_collection()

    def _load_data_and_create_collection(self):
        # Load food data
        with open(self.data_path, 'r', encoding='utf-8') as f:
            self.food_data = json.load(f)

        # Create or get collection
        try:
            self.collection = self.client.get_collection(self.collection_name)
            # Clear existing data to refresh
            all_docs = self.collection.get()
            self.collection.delete(ids=all_docs["ids"])
        except Exception:
            self.collection = self.client.get_or_create_collection(self.collection_name)

        # Prepare documents and embeddings
        documents = []
        ids = []
        metadatas = []
        for idx, item in enumerate(self.food_data):
            # Use item name and advisory as text for embedding
            text = item.get('item', '') + ". " + item.get('advisory', '')
            ids.append(str(idx))
            documents.append(text)
            # Convert list values in metadata to strings for ChromaDB compatibility
            # Also convert dict values to JSON string for compatibility
            safe_metadata = {}
            for k, v in item.items():
                if isinstance(v, list):
                    safe_metadata[k] = ", ".join(v)
                elif isinstance(v, dict):
                    safe_metadata[k] = json.dumps(v)
                else:
                    safe_metadata[k] = v
            metadatas.append(safe_metadata)

        # Add to collection
        self.collection.add(
            documents=documents,
            embeddings=[self.model.encode(doc).tolist() for doc in documents],
            metadatas=metadatas,
            ids=ids
        )
        # Persistence handled by client settings; no explicit persist call needed

    def retrieve_context(self, user_query, top_k=3):
        # Embed user query
        query_embedding = self.model.encode(user_query).tolist()
        # Query collection
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        # Extract metadatas of top results
        contexts = [result for result in results['metadatas'][0]]
        return contexts

    def get_food_info_by_name(self, item_name):
        """
        Retrieve structured food info by exact item name.
        """
        for item in self.food_data:
            if item.get('item', '').lower() == item_name.lower():
                return item
        return None

# Singleton instance for reuse
retriever = FoodRetriever()

def retrieve_context(user_query):
    return retriever.retrieve_context(user_query)

def get_food_info_by_name(item_name):
    return retriever.get_food_info_by_name(item_name)
