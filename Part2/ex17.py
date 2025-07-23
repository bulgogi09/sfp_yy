import random

# Step 1: Ask the user for their name
name = input("Welcome, agent. What is your name? ")

# Step 2 & 3: Create lists of adjectives and animals (6 each)
adjectives = ["Sneaky", "Brave", "Invisible", "Silent", "Witty", "Fierce"]
animals = ["Otter", "Panther", "Falcon", "Cobra", "Fox", "Jaguar"]

# Step 4 & 5: Randomly choose one adjective and one animal
adjective = random.choice(adjectives)
animal = random.choice(animals)
codename = f"{adjective} {animal}"

# Step 6: Generate a lucky number between 1 and 99
lucky_number = random.randint(1, 99)

# Step 7: Display the result using string formatting
print("\n🔍 Spy Profile Generated 🔍")
print(f"Agent {name}, your codename is: **{codename}**")
print(f"Your lucky number is: **{lucky_number}**")
