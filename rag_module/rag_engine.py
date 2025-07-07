from rag_module.retrieval import get_food_info_by_name
from rag_module.generate import generate_answer

def get_food_info(item_name):
    """
    Retrieve structured food info by item name for UI integration.
    """
    return get_food_info_by_name(item_name)

def rag_response(food_name):
    """
    Retrieve food info by name and generate a polite advisory response.
    """
    food_info = get_food_info_by_name(food_name)
    if not food_info:
        return f"Sorry, no information available for '{food_name}'."
    # Pass as list to generate_answer for compatibility
    return generate_answer(food_name, [food_info])

# Expose get_food_info and rag_response for import
__all__ = ['get_food_info', 'rag_response']
