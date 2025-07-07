import streamlit as st
from rag_module.rag_engine import rag_response
from pages.Home import show_home
from pages.Listings import show_listings
from pages.MapView import show_map
from pages.Reviews import show_reviews
from pages.Subscribe import show_subscribe

def add_global_styles():
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
            color: #333333;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .css-1d391kg {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .stButton>button {
            background-color: #ff5722;
            color: white;
            border-radius: 8px;
            padding: 8px 16px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #e64a19;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    st.set_page_config(page_title="Hyperlocal Tiffin Service", layout="wide")
    add_global_styles()

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Listings", "Map View", "Reviews", "Subscribe"])

    if page == "Home":
        show_home()
    elif page == "Listings":
        show_listings()
    elif page == "Map View":
        show_map()
    elif page == "Reviews":
        show_reviews()
    elif page == "Subscribe":
        show_subscribe()

    st.title("Hyperlocal Tiffin Service - Food Discovery")

    query = st.text_input("Ask about food items, ingredients, nutrients, or health advisories:")

    if query:
        st.write("Fetching answer...")
        answer = rag_response(query)
        st.write(answer)

if __name__ == "__main__":
    main()
