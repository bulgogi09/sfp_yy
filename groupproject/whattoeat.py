import streamlit as st
import requests

# ===== API Key =====
SPOONACULAR_API_KEY = "e6cf5cb8b84b49ecbe59feed47e7dc8c"

# ===== Background Image Function =====
def set_background(image_url, text_color="white"):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('{image_url}');
            background-size: cover;
            background-attachment: fixed;
        }}
        .content-container {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2em;
            border-radius: 15px;
        }}
        h1, h2, h3, h4, h5, h6, p, span, div {{
            color: {text_color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ===== Spoonacular Food Suggestion Function =====
def get_food_ideas(craving, max_calories):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "query": craving,
        "maxCalories": max_calories,
        "number": 5,
        "addRecipeInformation": True,
        "apiKey": SPOONACULAR_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("results", [])
    else:
        st.error(f"API error: {response.status_code}")
        return []

# ===== Dummy Restaurant Suggestions Function =====
def get_dummy_restaurants(craving, location):
    dummy_data = {
        "pizza": [
            {"name": "Joe's Pizza", "address": f"Main Street, {location}", "rating": 4.5},
            {"name": "Crusty Heaven", "address": f"2nd Ave, {location}", "rating": 4.2},
        ],
        "sushi": [
            {"name": "Sushi World", "address": f"Market Road, {location}", "rating": 4.7},
        ],
        "burger": [
            {"name": "Burger Town", "address": f"Downtown {location}", "rating": 4.3},
        ]
    }
    for key in dummy_data:
        if key in craving.lower():
            return dummy_data[key]
    return [{"name": "Local Bites", "address": f"Center St, {location}", "rating": 4.0}]

# ===== Streamlit App UI =====
st.set_page_config(page_title="What To Eat App", page_icon="🍽️", layout="centered")

# Set initial background
opening_background = "https://images.unsplash.com/photo-1546069901-ba9599a7e63c"
set_background(opening_background, text_color="white")

st.markdown("""
    <div class='content-container'>
        <h1 style='text-align: center;'>🍽️ What Should I Eat?</h1>
        <p style='text-align: center;'>Find meals and restaurant ideas based on your cravings and budget.</p>
    </div>
""", unsafe_allow_html=True)

# --- User Inputs ---
st.markdown("<div class='content-container'><h2>🔎 Enter Your Details</h2>", unsafe_allow_html=True)
with st.form("user_inputs"):
    location = st.text_input("📍 Your Location")
    budget = st.number_input("💰 Your Budget", min_value=1)
    currency = st.text_input("💱 Your Currency Symbol (e.g., $, €, ₹, RM)", value="$")
    craving = st.text_input("😋 What are you craving?")
    calories = st.number_input("🔥 Max Calories", min_value=100, max_value=2000, step=50)
    submitted = st.form_submit_button("🔍 Find Foods")
st.markdown("</div>", unsafe_allow_html=True)

# --- Results ---
if submitted:
    if craving and location:
        # Set new background after search
        results_background = "https://images.unsplash.com/photo-1504674900247-0877df9cc836"
        set_background(results_background, text_color="black")

        st.markdown("<div class='content-container'>", unsafe_allow_html=True)
        st.info("🔎 Searching for food options...")

        # ==== Spoonacular Recipes ====
        food_results = get_food_ideas(craving, calories)
        if food_results:
            st.markdown("### 🧑‍🍳 Recipe Suggestions")
            found = False
            for food in food_results:
                estimated_price = 10.00  # dummy price for now

                if estimated_price <= budget:
                    found = True
                    st.success(food["title"])
                    st.image(food["image"], use_column_width=True)
                    st.write(f"📍 Location: {location}")
                    st.write(f"💸 Estimated Price: {currency}{estimated_price}")
                    st.write(f"🔥 Calories: {calories} kcal")
                    st.write(f"🕐 Ready in {food['readyInMinutes']} minutes")
                    st.write(f"🍽️ Servings: {food['servings']}")
                    st.markdown(f"[🔗 View Recipe]({food['sourceUrl']})")
                    st.write("---")

            if not found:
                st.warning("🚫 No foods found within your budget. Try increasing your budget.")
        else:
            st.warning("🔍 No results found. Try a different craving or lower calorie limit.")

        # ==== Dummy Restaurant Suggestions ====
        st.markdown("### 🏪 Nearby Restaurant Suggestions")
        restaurants = get_dummy_restaurants(craving, location)
        if restaurants:
            for r in restaurants:
                st.markdown(f"**{r['name']}**")