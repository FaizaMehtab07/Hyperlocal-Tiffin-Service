Update Report: Food Advisory Feature (RAG Integration)

As part of my internship task, I extended my existing **Hyperlocal Tiffin Aggregator** project by integrating an AI-powered **Food Advisory** system using **RAG (Retrieval-Augmented Generation)** with the **Gemini API**.
To help users get **simple, useful, and polite health advisories** for food items they view in the app — based on real ingredients and nutrient data.

---

## How It Works

- A JSON file (`food_info.json`) was created containing ingredients, nutrients, and a soft health advisory.
- When users click **"Show Food Advisory"**, it triggers the **RAG pipeline**:
  1. **Retriever** module finds the correct food data from JSON.
  2. **Gemini API** (via `generate.py`) augments the input and generates a friendly advisory.
  3. The output is shown in the app interface, under the food item.
File Structure Updates

Inside main project:

├── rag_module/
│ ├── rag_engine.py # Main RAG handler
│ ├── retrieval.py # Vector/context retriever
│ └── generate.py # Gemini-powered advisory generator
├── data/
│ └── food_info.json # All food metadata used by RAG