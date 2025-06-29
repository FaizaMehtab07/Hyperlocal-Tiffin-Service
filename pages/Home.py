import streamlit as st

def show_home():
    st.markdown(
        """
        <div style="background-color:#ff5722; padding: 20px; border-radius: 10px;">
            <h1 style="color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                Welcome to the Hyperlocal Tiffin Service
            </h1>
            <p style="color: white; font-size: 18px;">
                Easily discover nearby, affordable, and hygienic daily meal providers.
            </p>
            <p style="color: white; font-size: 16px;">
                Navigate through the sidebar to explore listings, view map, read reviews, and manage subscriptions.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

