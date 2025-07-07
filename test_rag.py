from rag_module.retrieval import retrieve_context

def test_retrieval():
    query = "Diabetic friendly food with less oil"
    results = retrieve_context(query)
    print("Top Results:")
    for item in results:
        print(f"Name: {item['item']}")
        print(f"Advisory: {item['advisory']}")
        print("Ingredients:", ", ".join(item['ingredients']))
        print("Nutrients:", item['nutrients'])
        print("-" * 40)

if __name__ == "__main__":
    test_retrieval()
