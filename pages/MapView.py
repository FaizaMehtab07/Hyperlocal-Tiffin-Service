import streamlit as st
import streamlit_folium as st_folium
import folium

def show_map():
    st.header("Nearby Tiffin Services Map")

    data = [
        {"Name": "Homely Tiffins", "Location": [17.435, 78.394], "Area": "Gachibowli"},
        {"Name": "Spicy Meals", "Location": [17.443, 78.391], "Area": "Madhapur"},
        {"Name": "Healthy Bites", "Location": [17.450, 78.400], "Area": "Hitech City"},
        {"Name": "Tandoori Treats", "Location": [17.460, 78.410], "Area": "Kondapur"}
    ]

    m = folium.Map(location=[17.385, 78.4867], zoom_start=12)

    for service in data:
        folium.Marker(
            location=service["Location"],
            popup=f"{service['Name']} - {service['Area']}",
            tooltip=service["Name"]
        ).add_to(m)

    st_folium.folium_static(m)
