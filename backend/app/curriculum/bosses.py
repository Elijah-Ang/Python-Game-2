# Boss Levels - Integration Challenges
# Sand Sphinx (after Ch 1-4) and Final Boss (end)

BOSS_LEVELS = [
    {
        "id": 100,
        "title": "Sand Sphinx Boss",
        "slug": "sand-sphinx-boss",
        "icon": "🐍",
        "is_boss": True,
        "lessons": [
            {
                "id": 82,
                "title": "🐍 Sand Sphinx Challenge",
                "order": 1,
                "content": """# 🐍 BOSS BATTLE: The Sand Sphinx

The Sand Sphinx guards the way forward. To pass, you must prove your mastery of the fundamentals!

## The Challenge

Create a **mini program** that combines everything from Chapters 1-4:
- Variables & data types
- String manipulation
- Math operations
- Loops
- Conditionals
- Functions

## Your Mission

Build a simple **Number Guessing Game**:
1. Generate a random number 1-10
2. Let the user "guess" (we'll simulate with a variable)
3. Tell them if they're too high, too low, or correct
4. Keep track of attempts

---

## 🎯 Complete the Challenge
""",
                "starter_code": """import random

# Generate secret number
secret = random.randint(1, 10)
print(f"(Secret is: {secret})")  # For testing

# Simulate user guesses
guesses = [5, 8, 3, 7]  # Simulated guesses
attempts = 0

for guess in guesses:
    attempts += 1
    if guess == secret:
        print(f"Correct! It took {attempts} attempts.")
        break
    elif guess < secret:
        print(f"{guess} is too low!")
    else:
        print(f"{guess} is too high!")
else:
    print(f"Out of guesses! Secret was {secret}")
""",
                "xp": 50
            }
        ]
    },
    {
        "id": 101,
        "title": "Final Boss: Data Scientist",
        "slug": "final-boss",
        "icon": "💀",
        "is_boss": True,
        "lessons": [
            {
                "id": 83,
                "title": "💀 FINAL BOSS: Full Stack Data Scientist",
                "order": 1,
                "content": """# 💀 FINAL BOSS: The Full Stack Data Scientist

You've learned it all. Now combine everything into a complete data science workflow!

## The Ultimate Challenge

Create a complete **mini ML pipeline**:
1. Load/create data
2. Explore with statistics
3. Visualize patterns
4. Train a model
5. Evaluate performance

---

## 🎯 Complete the Full Pipeline
""",
                "starter_code": """import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1. Create data (house size -> price)
np.random.seed(42)
size = np.random.randint(500, 3000, 100).reshape(-1, 1)
price = size * 100 + np.random.normal(0, 10000, (100, 1))

# 2. Basic statistics
print(f"Size: mean={size.mean():.0f}, std={size.std():.0f}")
print(f"Price: mean={price.mean():.0f}, std={price.std():.0f}")

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(
    size, price, test_size=0.2, random_state=42
)

# 4. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"\\nModel R² Score: {r2:.4f}")
print(f"Price prediction for 2000 sqft: ${model.predict([[2000]])[0][0]:,.0f}")

print("\\n🎉 CONGRATULATIONS! You've completed the course!")
""",
                "xp": 100
            }
        ]
    }
]
