import google.generativeai as genai

# Gemini API key seting
# Make sure to set your API key in the environment variable or directly here
genai.configure(api_key="YOUR`S API KEY HERE")

# Best available model
MODEL = "models/gemini-2.0-flash-lite"

def generate_answer(user_query, context):
    """
    Generate a polite health advisory using Gemini.
    Args:
        user_query (str): Food item name.
        context (list): Food info dicts with ingredients, nutrients, advisory.
    """
    if not context or len(context) == 0:
        return f"Sorry, I have no information available for {user_query}."

    food_info = context[0]

    ingredients = ", ".join(food_info.get("ingredients", []))
    nutrients = ", ".join([f"{k}: {v}" for k, v in food_info.get("nutrients", {}).items()])
    advisory = food_info.get("advisory", "")

    prompt = (
    f"Generate a short, simple, and friendly food advisory for '{user_query}'. "
    f"Keep it polite, very easy to understand, and point-wise (maximum 3 short points). "
    f"Mention key ingredients: {ingredients}. Nutritional info: {nutrients}. "
    f"Include 1-2 health benefits or tips in simple language. "
    f"Advise portion control or how to balance the meal if needed. "
    f"Add a friendly reminder to avoid food waste like 'Don't waste food, every bite counts!'. "
    f"Make sure the tone is emotional, positive, and feels like everyday conversation, not strict or medical."
)

    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating advisory: {e}"
