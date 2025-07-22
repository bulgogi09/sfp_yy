import streamlit as st

# App title
st.title("🍽️ What Should I Eat?")

# Section: User Inputs
st.header("Tell us what you're looking for:")

location = st.text_input("📍 Your Location")
budget = st.number_input("💰 Budget (in your currency)", min_value=1)
preference = st.selectbox("🍴 Food Preference", ["Any", "Vegetarian", "Vegan", "Halal", "Non-Veg"])
craving = st.text_input("😋 Craving for... (e.g., pizza, sushi)")
calories = st.slider("🔥 Max Calories", 100, 2000, step=50)
nutrients = st.multiselect("🧪 Nutrient Focus", ["High Protein", "Low Carb", "Low Fat", "High Fiber"])

# Submit Button
if st.button("🔍 Find Food Options"):
    # In the future: Add logic here to recommend food
    st.success("✅ Processing your request...")

    # Dummy output (for now)
    st.subheader("🍔 Suggested Food")
    st.write("**Grilled Chicken Salad**")
    st.write("- 💸 Price: $8.99")
    st.write("- 📍 Store: Healthy Bites, Main Street")
    st.write("- ⭐ Rating: 4.5 / 5")
    st.write("- 🔥 Calories: 420 kcal")

currency = st.selectbox("💱 Choose your currency", ["USD ($)", "EUR (€)", "GBP (£)", "INR (₹)", "MYR (RM)", "JPY (¥)"])

