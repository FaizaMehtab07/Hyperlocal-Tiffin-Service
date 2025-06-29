import streamlit as st

def show_reviews():
    st.header("Rate & Review Services")

    services = ["Homely Tiffins", "Spicy Meals", "Healthy Bites", "Tandoori Treats"]
    selected = st.selectbox("Select Service", services)

    if "reviews" not in st.session_state:
        st.session_state.reviews = {
            "Homely Tiffins": [],
            "Spicy Meals": [],
            "Healthy Bites": [],
            "Tandoori Treats": []
        }

    rating = st.slider("Rating", 1, 5, 3)
    review = st.text_area("Write your review")

    if st.button("Submit Review"):
        st.session_state.reviews[selected].append({"rating": rating, "review": review})
        st.success(f"Thank you! Your {rating}-star review for {selected} has been submitted.")

    st.subheader(f"Reviews for {selected}")
    for r in st.session_state.reviews[selected]:
        st.write(f"Rating: {r['rating']} ⭐")
        st.write(f"Review: {r['review']}")
        st.markdown("---")
