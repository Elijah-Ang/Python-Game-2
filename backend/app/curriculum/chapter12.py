# Chapter 12: Machine Learning
# Enhanced with full detailed definitions and explanations

CHAPTER_12 = {
    "id": 14,
    "title": "Machine Learning Intro",
    "slug": "python-ml",
    "icon": "🤖",
    "is_boss": False,
    "lessons": [
        {
            "id": 104,
            "title": "Train/Test Split",
            "order": 1,
            "content": """# 🔀 Train/Test Split

## Why Split Data?

When building a machine learning model, you need to:
1. **Train** the model on part of your data
2. **Test** it on unseen data to see if it generalizes

If you test on the same data you trained on, you might just be memorizing, not learning!

## How It Works

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,    # 20% for testing
    random_state=42   # For reproducibility
)
```

## Typical Splits

| Training | Testing | Use Case |
| --- | --- | --- |
| 80% | 20% | Standard |
| 70% | 30% | Smaller datasets |
| 90% | 10% | Large datasets |

## Why random_state?

Setting `random_state` ensures the same split every time you run the code - essential for reproducible experiments!

## The Data

- **X**: Features (input variables)
- **y**: Target (what you're predicting)
- **X_train, y_train**: Used to train the model
- **X_test, y_test**: Used to evaluate the model

---

## 🎯 Your Task

Split X `[[1], [2], [3], [4], [5]]` and y `[1, 2, 3, 4, 5]` with 20% for testing (random_state=42). Print the number of training samples.
""",
            "starter_code": "from sklearn.model_selection import train_test_split\n\nX = [[1], [2], [3], [4], [5]]\ny = [1, 2, 3, 4, 5]\n\n# Split with random_state=42\n",
            "solution_code": "from sklearn.model_selection import train_test_split\n\nX = [[1], [2], [3], [4], [5]]\ny = [1, 2, 3, 4, 5]\n\n# Split with random_state=42\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\nprint(len(X_train))",
            "expected_output": "4",
            "xp": 10
        },
        {
            "id": 105,
            "title": "Linear Regression",
            "order": 2,
            "content": """# 📈 Linear Regression

## What is Linear Regression?

**Linear regression** finds the best straight line through your data. It's used to predict **continuous values** (like prices, temperatures, quantities).

## The Line Equation

$$y = mx + b$$

- **m**: slope (how much y changes when x changes)
- **b**: intercept (where the line crosses y-axis)

## Using Scikit-Learn

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)  # Learn from data
predictions = model.predict(X_test)  # Make predictions

# See the learned parameters
print(model.coef_)       # Slope(s)
print(model.intercept_)  # Intercept
```

## When to Use

- Predicting house prices from square footage
- Estimating sales from advertising spend
- Forecasting temperature from historical data

## Assumptions

Linear regression works best when:
- Relationship is roughly linear
- Data points are independent
- Errors are normally distributed

---

## 🎯 Your Task

Train a linear regression on X `[[1], [2], [3], [4], [5]]`, y `[2, 4, 6, 8, 10]` (y = 2x). Predict for X=6 and print the result.
""",
            "starter_code": "from sklearn.linear_model import LinearRegression\n\nX = [[1], [2], [3], [4], [5]]\ny = [2, 4, 6, 8, 10]\n\n# Train and predict for [[6]]\n",
            "solution_code": "from sklearn.linear_model import LinearRegression\n\nX = [[1], [2], [3], [4], [5]]\ny = [2, 4, 6, 8, 10]\n\n# Train and predict for [[6]]\nmodel = LinearRegression()\nmodel.fit(X, y)\nprediction = model.predict([[6]])\nprint(prediction[0])",
            "expected_output": "12.0",
            "xp": 10
        },
        {
            "id": 106,
            "title": "Model Accuracy",
            "order": 3,
            "content": """# 📊 Measuring Model Performance

## Classification Accuracy

For classification problems, accuracy is the percentage of correct predictions:

$$\\text{accuracy} = \\frac{\\text{correct predictions}}{\\text{total predictions}}$$

```python
from sklearn.metrics import accuracy_score

y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 0, 1, 0]

accuracy = accuracy_score(y_true, y_pred)
print(accuracy)  # 0.8 (80% correct)
```

## Interpreting Accuracy

- **100%**: Perfect (suspicious - might be overfitting!)
- **90%+**: Generally very good
- **50%**: No better than random guessing (for binary classification)

## Other Metrics

| Metric | Best For |
| --- | --- |
| Accuracy | Balanced classes |
| Precision | When false positives are costly |
| Recall | When false negatives are costly |
| F1-Score | Balance of precision and recall |

## Why Accuracy Isn't Everything

If 99% of emails are not spam, a model that predicts "not spam" for everything gets 99% accuracy but is useless!

Always consider the **context** of your problem.

---

## 🎯 Your Task

Calculate accuracy for true `[1, 0, 1, 1, 0]` vs predicted `[1, 0, 0, 1, 0]` and print it.
""",
            "starter_code": "from sklearn.metrics import accuracy_score\n\ny_true = [1, 0, 1, 1, 0]\ny_pred = [1, 0, 0, 1, 0]\n\n# Calculate accuracy\n",
            "solution_code": "from sklearn.metrics import accuracy_score\n\ny_true = [1, 0, 1, 1, 0]\ny_pred = [1, 0, 0, 1, 0]\n\n# Calculate accuracy\nacc = accuracy_score(y_true, y_pred)\nprint(acc)",
            "expected_output": "0.8",
            "xp": 10
        },
        {
            "id": 107,
            "title": "K-Nearest Neighbors",
            "order": 4,
            "content": """# 🎯 K-Nearest Neighbors (KNN)

## How KNN Works

KNN classifies based on the **k closest training examples**:

1. Pick a value for k (e.g., k=3)
2. Find the k nearest data points to your new point
3. Have them "vote" on the classification
4. Majority wins!

## Visual Example

```
Classifying ?: k=3

    O   O
  O   ?   X
    X   X
```

3 nearest neighbors: 2 X's, 1 O → Classify as X

## Using Scikit-Learn

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
```

## Choosing k

| k Value | Effect |
| --- | --- |
| Small (e.g., 1) | Sensitive to noise |
| Large (e.g., 15) | Smoother decision boundary |

**Tip**: Try odd numbers to avoid ties!

## Pros and Cons

✅ Simple and intuitive
✅ No training phase
❌ Slow for large datasets
❌ Sensitive to irrelevant features

---

## 🎯 Your Task

Train KNN (k=3) on X `[[0], [1], [2], [3]]`, y `[0, 0, 1, 1]`. Predict for X=1.5 and print the result.
""",
            "starter_code": "from sklearn.neighbors import KNeighborsClassifier\n\nX = [[0], [1], [2], [3]]\ny = [0, 0, 1, 1]\n\n# Train and predict for [[1.5]]\n",
            "solution_code": "from sklearn.neighbors import KNeighborsClassifier\n\nX = [[0], [1], [2], [3]]\ny = [0, 0, 1, 1]\n\n# Train and predict for [[1.5]]\nknn = KNeighborsClassifier(n_neighbors=3)\nknn.fit(X, y)\npred = knn.predict([[1.5]])\nprint(pred[0])",
            "expected_output": "0",
            "xp": 10
        },
        {
            "id": 108,
            "title": "Decision Tree",
            "order": 5,
            "content": """# 🌳 Decision Trees

## How Decision Trees Work

A decision tree learns a series of if-then rules:

```
Is age > 30?
├── Yes: Is income > 50K?
│   ├── Yes: Approve loan
│   └── No: Deny loan
└── No: Is credit good?
    ├── Yes: Approve loan
    └── No: Deny loan
```

## Using Scikit-Learn

```python
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)
predictions = tree.predict(X_test)
```

## Why Decision Trees Are Popular

✅ **Interpretable**: You can explain why a decision was made
✅ **Handles both numeric and categorical data**
✅ **Requires little data preprocessing**
✅ **Can capture non-linear relationships**

## Avoiding Overfitting

Unrestricted trees can memorize training data:

```python
# Limit tree depth
tree = DecisionTreeClassifier(max_depth=3)

# Require minimum samples to split
tree = DecisionTreeClassifier(min_samples_split=5)
```

## Visualizing Trees

```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plot_tree(tree, filled=True)
plt.show()
```

---

## 🎯 Your Task

Train a DecisionTree on X `[[1, 2], [1, 4], [4, 2], [4, 4]]`, y `[0, 0, 1, 1]`. Predict for `[[2, 3]]` and print the result.
""",
            "starter_code": "from sklearn.tree import DecisionTreeClassifier\n\nX = [[1, 2], [1, 4], [4, 2], [4, 4]]\ny = [0, 0, 1, 1]\n\n# Train and predict\n",
            "solution_code": "from sklearn.tree import DecisionTreeClassifier\n\nX = [[1, 2], [1, 4], [4, 2], [4, 4]]\ny = [0, 0, 1, 1]\n\n# Train and predict\ntree = DecisionTreeClassifier(random_state=42)\ntree.fit(X, y)\npred = tree.predict([[2, 3]])\nprint(pred[0])",
            "expected_output": "0",
            "xp": 10
        },
        {
            "id": 109,
            "title": "Feature Scaling",
            "order": 6,
            "content": """# ⚖️ Feature Scaling

## Why Scale Features?

Many algorithms perform poorly when features have different scales:

```
Feature 1: Age (range 0-100)
Feature 2: Income (range 0-1,000,000)
```

Without scaling, income dominates distance calculations!

## StandardScaler

Transforms data to have **mean=0** and **std=1**:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Mean is now ~0, std is now ~1
print(X_scaled.mean())  # Very close to 0
print(X_scaled.std())   # Very close to 1
```

## Other Scalers

| Scaler | Range | Use Case |
| --- | --- | --- |
| StandardScaler | Mean=0, Std=1 | Most algorithms |
| MinMaxScaler | 0 to 1 | Neural networks |
| RobustScaler | Based on median | Outliers present |

## Algorithms That Need Scaling

- K-Nearest Neighbors (distance-based)
- SVM (distance-based)
- Neural Networks
- Linear Regression (for interpretation)

## Algorithms That Don't Need Scaling

- Decision Trees
- Random Forests
- XGBoost

---

## 🎯 Your Task

Scale `[[1, 100], [2, 200], [3, 300]]` using StandardScaler and print the mean of the scaled data (should be ~0).
""",
            "starter_code": "from sklearn.preprocessing import StandardScaler\nimport numpy as np\n\nX = [[1, 100], [2, 200], [3, 300]]\n\n# Scale and print mean\n",
            "solution_code": "from sklearn.preprocessing import StandardScaler\nimport numpy as np\n\nX = [[1, 100], [2, 200], [3, 300]]\n\n# Scale and print mean\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(X)\nprint(round(np.mean(X_scaled), 1))",
            "expected_output": "0.0",
            "xp": 10
        },
        {
            "id": 110,
            "title": "Cross Validation",
            "order": 7,
            "content": """# 🔄 Cross Validation

## Why Cross Validate?

A single train/test split might be lucky or unlucky. **Cross validation** gives more reliable performance estimates.

## K-Fold Cross Validation

1. Split data into k equal parts (folds)
2. Train on k-1 folds, test on remaining fold
3. Repeat k times, each fold being the test set once
4. Average the results!

```
Fold 1: [Test] [Train] [Train] [Train] [Train]
Fold 2: [Train] [Test] [Train] [Train] [Train]
Fold 3: [Train] [Train] [Test] [Train] [Train]
Fold 4: [Train] [Train] [Train] [Test] [Train]
Fold 5: [Train] [Train] [Train] [Train] [Test]
```

## Using Scikit-Learn

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
print(f"Scores: {scores}")
print(f"Mean: {scores.mean():.2f}")
print(f"Std: {scores.std():.2f}")
```

## Choosing k

- **k=5 or k=10**: Most common, good balance
- **k=n (Leave-One-Out)**: Maximum data for training, but expensive

---

## 🎯 Your Task

Use 3-fold cross validation on LinearRegression with X `[[1], [2], [3], [4], [5], [6]]`, y `[1, 2, 3, 4, 5, 6]`. Print the mean score rounded to 2 decimals.
""",
            "starter_code": "from sklearn.model_selection import cross_val_score\nfrom sklearn.linear_model import LinearRegression\n\nX = [[1], [2], [3], [4], [5], [6]]\ny = [1, 2, 3, 4, 5, 6]\n\n# Cross validation\n",
            "solution_code": "from sklearn.model_selection import cross_val_score\nfrom sklearn.linear_model import LinearRegression\n\nX = [[1], [2], [3], [4], [5], [6]]\ny = [1, 2, 3, 4, 5, 6]\n\n# Cross validation\nmodel = LinearRegression()\nscores = cross_val_score(model, X, y, cv=3)\nprint(round(scores.mean(), 2))",
            "expected_output": "1.0",
            "xp": 10
        },
        {
            "id": 111,
            "title": "Confusion Matrix",
            "order": 8,
            "content": """# 📊 Confusion Matrix

## What is a Confusion Matrix?

A table showing the breakdown of predictions vs actual values:

```
                Predicted
              |  0  |  1  |
Actual   0    | TN  | FP  |
         1    | FN  | TP  |
```

- **TN (True Negative)**: Correctly predicted negative
- **TP (True Positive)**: Correctly predicted positive
- **FP (False Positive)**: Wrongly predicted positive (Type I error)
- **FN (False Negative)**: Wrongly predicted negative (Type II error)

## Using Scikit-Learn

```python
from sklearn.metrics import confusion_matrix

y_true = [0, 0, 1, 1]
y_pred = [0, 1, 1, 1]

cm = confusion_matrix(y_true, y_pred)
print(cm)
# [[1 1]
#  [0 2]]
```

## Reading the Matrix

```
[[1 1]     TN=1, FP=1
 [0 2]]    FN=0, TP=2
```

- 1 true negative (correctly said 0)
- 1 false positive (said 1, was actually 0)
- 0 false negatives
- 2 true positives

## Derived Metrics

- **Precision**: TP / (TP + FP) - How accurate are positive predictions?
- **Recall**: TP / (TP + FN) - How many positives did we catch?

---

## 🎯 Your Task

Create a confusion matrix for true `[0, 0, 1, 1]` vs predicted `[0, 1, 1, 1]` and print it.
""",
            "starter_code": "from sklearn.metrics import confusion_matrix\n\ny_true = [0, 0, 1, 1]\ny_pred = [0, 1, 1, 1]\n\n# Print confusion matrix\n",
            "solution_code": "from sklearn.metrics import confusion_matrix\n\ny_true = [0, 0, 1, 1]\ny_pred = [0, 1, 1, 1]\n\n# Print confusion matrix\ncm = confusion_matrix(y_true, y_pred)\nprint(cm)",
            "expected_output": "[[1 1]\n [0 2]]",
            "xp": 10
        },
        {
            "id": 112,
            "title": "Complete ML Pipeline",
            "order": 9,
            "content": """# 🎯 Putting It All Together

## The Machine Learning Workflow

A typical ML project follows these steps:

```
1. Understand the problem
2. Prepare the data
3. Choose a model
4. Train the model
5. Evaluate performance
6. Tune and improve
7. Deploy
```

## A Simple Pipeline

```python
# 1. Load data
X = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]

# 2. Split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 3. Choose and train model
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)

# 4. Make predictions
predictions = model.predict(X_test)

# 5. Evaluate
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))
```

## Tips for Success

- **Start simple**: Try a basic model first
- **Iterate**: Improve gradually based on results
- **Validate properly**: Use cross-validation
- **Understand your data**: Visualization helps!

---

## 🎯 Your Task

Build a complete classifier: Create data X `[[1], [2], [3], [4]]`, y `[0, 0, 1, 1]`. Train KNeighborsClassifier (k=1) and predict for X=2.5. Print the prediction.
""",
            "starter_code": "from sklearn.neighbors import KNeighborsClassifier\n\nX = [[1], [2], [3], [4]]\ny = [0, 0, 1, 1]\n\n# Complete pipeline\n",
            "solution_code": "from sklearn.neighbors import KNeighborsClassifier\n\nX = [[1], [2], [3], [4]]\ny = [0, 0, 1, 1]\n\n# Complete pipeline\nmodel = KNeighborsClassifier(n_neighbors=1)\nmodel.fit(X, y)\nprediction = model.predict([[2.5]])\nprint(prediction[0])",
            "expected_output": "0",
            "xp": 10
        }
    ]
}
