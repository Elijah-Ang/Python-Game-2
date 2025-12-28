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
                "id": 40,
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
                "starter_code": """# Write your Number Guessing Game here
import random

# Step 1: Generate secret number (1-10)


# Step 2: Create a list of guesses to simulate user input
# guesses = [5, 8, 3, 7]


# Step 3: Track attempts


# Step 4: Loop through guesses and provide feedback

""",
                "solution_code": """import random

# Generate secret number
random.seed(42)  # For consistent testing
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
                "expected_output": "(Secret is: 2)\n5 is too high!\n8 is too high!\n3 is too high!\nOut of guesses! Secret was 2",
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
                "id": 113,
                "title": "💀 FINAL BOSS: Full Stack Data Scientist",
                "order": 1,
                "content": """# 💀 FINAL BOSS: The Full Stack Data Scientist

Congratulations on making it this far! You've mastered Python fundamentals, data manipulation, visualization, statistics, and machine learning. Now it's time to prove your skills by building a **complete end-to-end data science pipeline**.

---

## 🏆 The Ultimate Challenge

You are a data scientist at a real estate company. Your task is to build a **house price prediction model** using the skills you've learned throughout this course.

## 📋 Your Mission

Complete ALL of the following steps:

### Step 1: Create the Dataset
Generate synthetic house data with:
- **Features**: House size (square feet)
- **Target**: House price (with some realistic noise)
- Use `np.random.seed(42)` for reproducibility

### Step 2: Explore the Data
Calculate and print basic statistics:
- Mean and standard deviation of house sizes
- Mean and standard deviation of house prices

### Step 3: Split the Data
Use `train_test_split` to create:
- 80% training data
- 20% test data
- Use `random_state=42`

### Step 4: Train a Model
- Create a `LinearRegression` model
- Fit it on the training data

### Step 5: Evaluate Performance
- Make predictions on test data
- Calculate and print the R² score
- Make a price prediction for a 2000 sqft house

### Step 6: Celebrate! 🎉
Print a congratulations message!

---

## 📊 Expected Output Format

Your output should look like this:
```
Size: mean=XXXX, std=XXX
Price: mean=XXXXXX, std=XXXXX

Model R² Score: 0.XXXX
Price prediction for 2000 sqft: $XXX,XXX

🎉 CONGRATULATIONS! You've completed the course!
```

---

## 💡 Hints

- Import: `numpy`, `train_test_split`, `LinearRegression`, `r2_score`
- Use `.reshape(-1, 1)` to make arrays 2D for sklearn
- Use f-strings with formatting: `f"{value:.2f}"` for 2 decimals
- Use `{value:,.0f}` for comma-separated numbers

---

## 🎯 Complete the Pipeline Below
""",
                "starter_code": """import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Step 1: Create the Dataset
# Generate 100 houses with sizes between 500-3000 sqft
# Price = size * 100 + random noise


# Step 2: Explore the Data
# Print mean and std for size and price


# Step 3: Split the Data (80/20 split)


# Step 4: Train a Linear Regression Model


# Step 5: Evaluate - Calculate R² and predict for 2000 sqft


# Step 6: Print congratulations message
""",
                "solution_code": """import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Step 1: Create the Dataset
np.random.seed(42)
size = np.random.randint(500, 3000, 100).reshape(-1, 1)
price = size * 100 + np.random.normal(0, 10000, (100, 1))

# Step 2: Explore the Data
print(f"Size: mean={size.mean():.0f}, std={size.std():.0f}")
print(f"Price: mean={price.mean():.0f}, std={price.std():.0f}")

# Step 3: Split the Data (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(
    size, price, test_size=0.2, random_state=42
)

# Step 4: Train a Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Evaluate - Calculate R² and predict for 2000 sqft
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"\\nModel R² Score: {r2:.4f}")
print(f"Price prediction for 2000 sqft: ${model.predict([[2000]])[0][0]:,.0f}")

# Step 6: Print congratulations message
print("\\n🎉 CONGRATULATIONS! You've completed the course!")""",
                "expected_output": """Size: mean=1716, std=712
Price: mean=171620, std=71218

Model R² Score: 0.9808
Price prediction for 2000 sqft: $199,917

🎉 CONGRATULATIONS! You've completed the course!""",
                "xp": 100
            }
        ]
    }
]
