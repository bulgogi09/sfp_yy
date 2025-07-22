import random

# List of flowers
flowers = ['rose', 'tulip', 'lily']

# Set the random seed to make the output predictable
random.seed(1)

# 1. Print a random flower from the list
print(random.choice(flowers))  # Always prints 'rose' with this seed

# 2. Print a random number from 0 to 100
print(random.randint(0, 100))  # Always prints 94 with this seed

