import streamlit as st
from PIL import Image
import os

# --- DATA DEFINITIONS ---
# It's good practice to define your data outside the main rendering function
# so it's not redefined on every interaction.

# Realistic descriptions for menu items
DESCRIPTIONS = {
    "Morning Bheja Fry": "200g spicy Hyderabadi brain fry, rich in flavor, serves 1",
    "Guddhe Fry": "150g fresh intestine fry, street-style tadka, serves 1",
    "Paya Soup": "Full bowl slow-cooked mutton trotters soup, healthy for joints",
    "Khichdi Khatta": "300g mildly spiced khichdi with tangy khatta, serves 1",
    "Bagara Khana with Dalcha": "Aromatic Hyderabadi bagara rice with dalcha curry, serves 1",
    "Phulkas": "2 soft homemade phulkas with pickle",
    "Plain White Rice": "350g steamed plain white rice, fresh & hot",
    "Idli": "2 soft idlis with chutney & sambar, steamed to perfection",
    "Dosa": "Plain dosa with chutney & sambar, zero oil option available",
    "Mysore Dosa": "Spicy Mysore dosa with chutney, crispy edges, fluffy inside",
    "Mysore Bonda": "4 fluffy Mysore bondas with coconut chutney dip",
    "Curd Rice": "400g curd rice with fresh tempering, cooling and light",
    "Upma": "250g healthy semolina upma, light oil, served hot",
    "Pongal": "300g creamy ven pongal with ghee and pepper tadka",
    "Oats": "1 bowl oats with fruits, high fibre, zero oil, serves 1",
    "Vegetable Salad": "300g fresh mixed veggie salad with olive oil drizzle",
    "Russian Salad": "250g mildly sweet creamy Russian salad",
    "Chicken Salad": "200g grilled chicken salad with greens, lean protein, low oil",
    "Boiled Eggs": "2 perfectly boiled eggs, salt & pepper provided",
    "Sprouts Mix": "250g protein-rich sprouts salad with lemon dressing",
    "Bhindi Roti": "2 rotis with medium bowl of bhindi fry, homemade style",
    "Ragi Roti": "1 Ragi Roti, bajra/jowar options available",
    "Aloo Paratha": "2 stuffed aloo rotis with side raita",
    "Palak Paneer": "200g creamy spinach and paneer curry, mild spices",
    "Methi Ki Bhaji": "Small bowl methi stir fry, nutritious and low oil",
    "Vegetable Sabji": "350g mixed vegetable sabji, seasonal veggies, Aloo Gobi, etc.",
    "Rasam Rice": "Hot rasam with rice, comfort food, tangy and spicy",
    "Mixed Vegetable Khichdi": "Nutritious, zero masala veg khichdi, serves 1",
    "Spinach Juice": "300ml fresh spinach juice, rich in iron, zero sugar option",
    "ABC Juice": "300ml Apple-Beetroot-Carrot juice, detox drink",
    "Pomegranate Juice": "300ml fresh anar juice, with/without sugar option",
    "Apple Juice": "300ml fresh apple juice, chilled, no sugar option",
    "Orange Juice": "300ml fresh orange juice, Vitamin C boost",
    "Fresh Lemonade": "300ml chilled lemonade with mint, low sugar option",
}

# Menu categories with fixed image paths (Corrected .png.jpg to .jpg)
CATEGORIES = {
    "Hyderabadi Tiffin Specials": [
        {"Item": "Morning Bheja Fry", "Price": 60, "Type": "Non-Veg", "Image": "assets/bheja_fry.png.jpg"},
        {"Item": "Paya Soup", "Price": 70, "Type": "Non-Veg", "Image": "assets/paya_soup.png.jpg"},
        {"Item": "Khichdi Khatta", "Price": 40, "Type": "Veg", "Image": "assets/khichdi_khatta.png.jpg"},
        {"Item": "Bagara Khana with Dalcha", "Price": 80, "Type": "Veg", "Image": "assets/bagara_khana.png.jpg"},
        {"Item": "Phulkas", "Price": 20, "Type": "Veg", "Image": "assets/phulkas.png.jpg"},
        {"Item": "Plain White Rice", "Price": 30, "Type": "Veg", "Image": "assets/plain_rice.png.jpg"},
    ],
    "South Indian Tiffin": [
        {"Item": "Idli", "Price": 30, "Type": "Veg", "Image": "assets/idli.png.jpg"},
        {"Item": "Dosa", "Price": 50, "Type": "Veg", "Image": "assets/dosa.png.jpg"},
        {"Item": "Mysore Bonda", "Price": 40, "Type": "Veg", "Image": "assets/mysore_bonda.png.jpg"},
        {"Item": "Curd Rice", "Price": 50, "Type": "Veg", "Image": "assets/curd_rice.png.jpg"},
        {"Item": "Upma", "Price": 35, "Type": "Veg", "Image": "assets/upma.png.jpg"},
        {"Item": "Pongal", "Price": 45, "Type": "Veg", "Image": "assets/pongal.png.jpg"},
    ],
    "Diet & Zero-Calorie Tiffin": [
        {"Item": "Oats", "Price": 40, "Type": "Veg", "Image": "assets/oats.png.jpg"},
        {"Item": "Vegetable Salad", "Price": 50, "Type": "Veg", "Image": "assets/vegetable_salad.png.jpg"},
        {"Item": "Russian Salad", "Price": 60, "Type": "Veg", "Image": "assets/russian_salad.png.jpg"},
        {"Item": "Chicken Salad", "Price": 80, "Type": "Non-Veg", "Image": "assets/chicken_salad.png.jpg"},
        {"Item": "Boiled Eggs", "Price": 30, "Type": "Non-Veg", "Image": "assets/boiled_eggs.png.jpg"},
        {"Item": "Sprouts Mix", "Price": 40, "Type": "Veg", "Image": "assets/sprouts_mix.png.jpg"},
    ],
    "Homely Tiffin (Pure Ghar Ka Khana)": [
        {"Item": "Bhindi Roti", "Price": 40, "Type": "Veg", "Image": "assets/bhindi_roti.jpg"},
        {"Item": "Ragi Roti", "Price": 10, "Type": "Veg", "Image": "assets/Ragi_Roti.jpg"},
        {"Item": "Aloo Paratha", "Price": 40, "Type": "Veg", "Image": "assets/aloo_roti.jpg"},
        {"Item": "Palak Paneer", "Price": 70, "Type": "Veg", "Image": "assets/palak_paneer.jpg"},
        {"Item": "Vegetable Sabji", "Price": 50, "Type": "Veg", "Image": "assets/veg_sabji.jpg"},
        {"Item": "Rasam Rice", "Price": 40, "Type": "Veg", "Image": "assets/rasam_rice.jpg"},
        {"Item": "Mixed Vegetable Khichdi", "Price": 50, "Type": "Veg", "Image": "assets/mixed_vegetable_khichdi.jpg"},
    ],
    "Fresh Juices": [
        {"Item": "Spinach Juice", "Price": 40, "Type": "Veg", "Image": "assets/spinach_juice.jpg"},
        {"Item": "ABC Juice", "Price": 50, "Type": "Veg", "Image": "assets/abc_juice.jpg"},
        {"Item": "Pomegranate Juice", "Price": 60, "Type": "Veg", "Image": "assets/pomegranate_juice.jpg"},
        {"Item": "Apple Juice", "Price": 50, "Type": "Veg", "Image": "assets/apple_juice.jpg"},
        {"Item": "Orange Juice", "Price": 50, "Type": "Veg", "Image": "assets/orange_juice.jpg"},
        {"Item": "Fresh Lemonade", "Price": 40, "Type": "Veg", "Image": "assets/fresh_lemonade.jpg"},
    ],
}

# Define Tiffin Services
SERVICES = [
    {
        "Name": "Hyderabadi Tiffin Specials",
        "Area": "Shah Ali Banda",
        "Description": "Authentic Hyderabadi flavors – Bheja Fry, Khichdi Khatta, Paya Soup & more, pure street-style.",
        "Rating": 4.8,
        "Image": "assets/hyderabadi_tiffin.jpg",
        "Menu": CATEGORIES["Hyderabadi Tiffin Specials"]
    },
    {
        "Name": "South Indian Tiffin",
        "Area": "Mehdipatnam",
        "Description": "Classic South Indian breakfasts – Idli, Dosa, Pongal, Upma & Mysore specials, served fresh.",
        "Rating": 4.6,
        "Image": "assets/south_indian_tiffin.jpg",
        "Menu": CATEGORIES["South Indian Tiffin"]
    },
    {
        "Name": "Diet & Zero-Calorie Tiffin",
        "Area": "Tolichowki",
        "Description": "Healthy, calorie-conscious options – Salads, Oats, Boiled Eggs & High-Protein sprouts.",
        "Rating": 4.7,
        "Image": "assets/diet_tiffin.jpg",
        "Menu": CATEGORIES["Diet & Zero-Calorie Tiffin"]
    },
    {
        "Name": "Homely Tiffin (Pure Ghar Ka Khana)",
        "Area": "Gacchi Bowli",
        "Description": "Comforting home-cooked meals – Bhindi Roti, Baingan Bharta, Rasam Rice & more.",
        "Rating": 4.9,
        "Image": "assets/homely_tiffin.jpg",
        "Menu": CATEGORIES["Homely Tiffin (Pure Ghar Ka Khana)"]
    },
    {
        "Name": "Fresh Juices",
        "Area": "Chandrayangutta",
        "Description": "Refreshing healthy juices – Spinach, ABC Detox, Pomegranate & Sugar-free Lemonades.",
        "Rating": 4.5,
        "Image": "assets/fresh_juices.jpg",
        "Menu": CATEGORIES["Fresh Juices"]
    }
]

# --- HELPER FUNCTIONS ---

def load_image(image_path):
    """Loads an image from the given path, returns None if it doesn't exist."""
    if os.path.exists(image_path):
        try:
            return Image.open(image_path)
        except Exception as e:
            st.error(f"Error loading image {image_path}: {e}")
            return None
    return None

def get_service_food_types(service):
    """Checks the types of food available in a service's menu."""
    types = {item['Type'] for item in service['Menu']}
    return types

# --- MAIN APP FUNCTION ---

def show_listings():
    """Renders the main tiffin service listing page."""
    
    # Initialize cart in session state if it doesn't exist
    if 'cart' not in st.session_state:
        st.session_state.cart = []

    # Custom CSS for styling the page
    st.markdown(
        """
        <style>
            /* Main container for service card */
            .service-card {
                background-color: #FFFACD; /* Lemon Chiffon */
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                border: 1px solid #FFD700; /* Gold */
            }
            /* Style for menu item containers */
            .menu-item-container {
                background-color: #FFFFFF;
                border-radius: 8px;
                padding: 15px;
                margin-bottom: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                transition: box-shadow 0.3s ease;
            }
            .menu-item-container:hover {
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            /* Cart count indicator */
            .cart-count {
                position: fixed;
                top: 10px;
                right: 15px;
                background-color: #FF4B4B;
                color: white;
                padding: 8px 15px;
                border-radius: 50px;
                font-weight: bold;
                z-index: 1000;
                box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display cart count on top-right corner
    st.markdown(f"<div class='cart-count'>🛒 Cart: {len(st.session_state.cart)}</div>", unsafe_allow_html=True)

    st.header("Explore Tiffin Services in Hyderabad")
    st.write("") # Add some space

    # --- FILTERING AND SEARCH ---
    col1, col2 = st.columns([3, 1])
    with col1:
        search_term = st.text_input("Search by Tiffin Service Name", placeholder="e.g., Homely Tiffin")
    with col2:
        food_type_filter = st.selectbox("Filter by Food Type", ["All", "Veg", "Non-Veg"])

    # Filter logic
    filtered_services = []
    for service in SERVICES:
        # Search term filter
        name_match = search_term.lower() in service["Name"].lower()
        
        # Food type filter
        service_types = get_service_food_types(service)
        if food_type_filter == "All":
            type_match = True
        elif food_type_filter == "Veg":
            # Show services that have at least one veg item, or are purely veg
            type_match = "Veg" in service_types
        elif food_type_filter == "Non-Veg":
            # Show services that have at least one non-veg item
            type_match = "Non-Veg" in service_types
        else:
            type_match = True
        
        if name_match and type_match:
            filtered_services.append(service)

    if not filtered_services:
        st.warning("No services found matching your criteria.")
        return

    service_names = [service["Name"] for service in filtered_services]
    selected_service_name = st.selectbox("Select a Tiffin Service to see their menu", service_names)

    selected_service = next((s for s in filtered_services if s["Name"] == selected_service_name), None)

    # --- DISPLAY SELECTED SERVICE AND MENU ---
    if selected_service:
        st.markdown("---")
        with st.container():
            st.markdown(f"<div class='service-card'>", unsafe_allow_html=True)
            
            img = load_image(selected_service["Image"])
            if img:
                st.image(img, use_column_width=True, caption=f"Welcome to {selected_service['Name']}")
            
            st.subheader(selected_service['Name'])
            st.write(f"**Description:** {selected_service['Description']}")
            
            # Rating and Food Type Badges
            col1, col2 = st.columns(2)
            with col1:
                stars = "⭐" * int(round(selected_service["Rating"]))
                st.write(f"**Rating:** {stars} ({selected_service['Rating']})")
            with col2:
                service_types = get_service_food_types(selected_service)
                if "Non-Veg" in service_types and "Veg" in service_types:
                    badge = "Mixed (Veg & Non-Veg) 🟢🔴"
                elif "Non-Veg" in service_types:
                    badge = "Non-Veg Only 🔴"
                else:
                    badge = "Veg Only 🟢"
                st.write(f"**Food Type:** {badge}")

            st.markdown("</div>", unsafe_allow_html=True)

            # --- MENU DISPLAY ---
            st.markdown("### Menu Items")

            for item in selected_service["Menu"]:
                with st.container():
                    st.markdown("<div class='menu-item-container'>", unsafe_allow_html=True)
                    col1, col2, col3 = st.columns([1, 4, 1.5])
                    
                    with col1:
                        item_img = load_image(item["Image"])
                        if item_img:
                            st.image(item_img, width=80)
                    
                    with col2:
                        veg_emoji = "🟢" if item["Type"] == "Veg" else "🔴"
                        st.markdown(f"**{item['Item']}** {veg_emoji}")
                        desc = DESCRIPTIONS.get(item['Item'], "A delicious food item.")
                        st.write(desc)
                        st.markdown(f"**Price: ₹{item['Price']}**")
                    
                    with col3:
                        # Use a unique key for each button to avoid Streamlit errors
                        if st.button("Add to Cart", key=f"add_{selected_service_name}_{item['Item']}"):
                            # Create a copy to avoid modifying the original dict
                            item_to_add = item.copy()
                            item_to_add['service'] = selected_service_name # Track which service it came from
                            st.session_state.cart.append(item_to_add)
                            st.success(f"Added {item['Item']} to cart!")
                            # Rerun to update the cart count immediately
                            st.experimental_rerun()
                    
                    st.markdown("</div>", unsafe_allow_html=True)


# --- To run this file directly ---
if __name__ == "__main__":
    st.set_page_config(page_title="Tiffin Services", layout="centered")
    show_listings()
