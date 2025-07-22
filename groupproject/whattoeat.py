import streamlit as st
import requests

# ===== API Keys =====
SPOONACULAR_API_KEY = "e6cf5cb8b84b49ecbe59feed47e7dc8c"

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
st.title("🍽️ What Should I Eat? (With Dummy Restaurant Suggestions)")

# --- User Inputs ---
location = st.text_input("📍 Your Location")
budget = st.number_input("💰 Your Budget", min_value=1)
currency = st.text_input("💱 Your Currency Symbol (e.g., $, €, ₹, RM)", value="$")
craving = st.text_input("😋 What are you craving?")
calories = st.number_input("🔥 Max Calories", min_value=100, max_value=2000, step=50)

# --- Button to Search ---
if st.button("🔍 Find Foods"):
    if craving and location:
        st.info("Searching for food options...")

        # ==== Spoonacular Recipes ====
        food_results = get_food_ideas(craving, calories)
        if food_results:
            found = False
            for food in food_results:
                estimated_price = 10.00  # dummy price for now

                if estimated_price <= budget:
                    found = True
                    st.subheader(food["title"])
                    st.image(food["image"])
                    st.write(f"📍 Location: {location}")
                    st.write(f"💸 Estimated Price: {currency}{estimated_price}")
                    st.write(f"🔥 Calories: {calories} kcal")
                    st.write(f"🕐 Ready in {food['readyInMinutes']} minutes")
                    st.write(f"🍽️ Servings: {food['servings']}")
                    st.markdown(f"[🔗 View Recipe]({food['sourceUrl']})")
                    st.write("---")

            if not found:
                st.warning("No foods found within your budget. Try increasing your budget.")
        else:
            st.warning("No results found. Try a different craving or lower calorie limit.")

        # ==== Dummy Restaurant Suggestions ====
        st.subheader("🏪 Nearby Restaurant Suggestions")
        restaurants = get_dummy_restaurants(craving, location)
        if restaurants:
            for r in restaurants:
                st.markdown(f"**{r['name']}**")
                st.write(f"📍 {r['address']}")
                st.write(f"⭐ Rating: {r['rating']}")
                st.write("---")
        else:
            st.warning("No nearby restaurants found.")
    else:
        st.warning("Please enter both location and craving.")






