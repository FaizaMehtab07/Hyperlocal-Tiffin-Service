import streamlit as st

def show_subscribe():
    st.header("Subscription Plans")

    services = ["Homely Tiffins", "Spicy Meals", "Healthy Bites", "Tandoori Treats"]
    selected = st.selectbox("Select Service", services)

    plan = st.radio("Choose Plan", ["Daily", "Weekly", "Monthly"])

    st.write(f"Subscribe to {selected} with the plan that suits you best.")

    if st.button("Subscribe"):
        st.success(f"You have subscribed to {selected} on a {plan} basis.")
