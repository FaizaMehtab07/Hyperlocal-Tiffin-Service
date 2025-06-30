
# Hyperlocal Tiffin Service 🍽️

A Streamlit-based platform designed to help users discover, explore, and review nearby Tiffin & Mess services. Inspired by apps like Zomato & Swiggy, this system is tailored for hyperlocal, homemade, and authentic food options within the city.

---

## 💡 Project Idea

The project aims to solve the problem of finding reliable, homemade, and diet-conscious Tiffin services, especially for students, working professionals, and people new to the city. Unlike traditional food delivery platforms, this focuses on:

* Verified Tiffin & Mess services
* Home-style meals with dietary options
* Transparent reviews and ratings
* Hyperlocal availability within defined areas

---

## ✅ Current Implementation Status

Modular project structure implemented
Service listing with category-wise filtering (Veg/Non-Veg)
Realistic food menus with item-wise images and details
Add to Cart functionality with session management
Basic Reviews system for user feedback
Yellow-themed UI with engaging, food-friendly design
Search and Filter by Service Name or Area
Basic authentication setup in progress

**Total Progress:** Approximately 30% complete
**Pending Major Features:**

* Cart checkout with transaction summary
* Interactive map view for location-based services
* Order confirmation workflow
* Enhanced responsive design for mobile screens
* Complete authentication & subscription system

Work is being implemented feature-by-feature with a focus on visual improvements and user experience.

---

## 📁 Project Folder Structure

```
IDEA_TIFFIN/
├── .streamlit/
│   └── config.toml         # Streamlit theme configuration
├── assets/                 # Food images and media assets
├── pages/
│   ├── Home.py             # Landing/Home page
│   ├── Listings.py         # Tiffin services listings & menu
│   ├── MapView.py          # Map view (under development)
│   ├── Reviews.py          # Reviews & Ratings page
│   └── Subscribe.py        # Subscription/Sign-up (under development)
├── app.py                  # Main Streamlit entry point with navigation
├── auth.py                 # Basic authentication logic
├── db.py                   # Database setup and operations
├── requirements.txt        # Python package dependencies
└── README.md               # Project overview and instructions
```

---

## 🌐 Live Deployment

Test the app live here:
**[https://faizamehtab-hyperlocal-tiffin-service.streamlit.app](https://faizamehtab-hyperlocal-tiffin-service.streamlit.app)**

---

## ⚙️ How to Clone & Run Locally

```bash
git clone https://github.com/your-username/hyperlocal-tiffin-service.git
cd hyperlocal-tiffin-service
pip install -r requirements.txt
streamlit run app.py
```

---

* Some images may require resizing for uniform display
* Features like Cart checkout and MapView are work-in-progress
* Yellow color theme used to create a food-craving friendly vibe
* Ideal for students, hostel residents, or office-goers
