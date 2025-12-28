# Chapter 12: Machine Learning
CHAPTER_12 = {
    "id": 13,
    "title": "Machine Learning Intro",
    "slug": "python-ml",
    "icon": "🤖",
    "is_boss": False,
    "lessons": [
        {
            "id": 103,
            "title": "Train/Test Split",
            "order": 1,
            "content": """# 🔀 Train/Test Split

Split data for training and testing:

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

---

## 🎯 Your Task

Split this data with 20% for testing:
- X: `[[1], [2], [3], [4], [5]]`
- y: `[1, 2, 3, 4, 5]`

Print the number of training samples.
Use `random_state=42` for reproducibility.
""",
            "starter_code": "from sklearn.model_selection import train_test_split\n\nX = [[1], [2], [3], [4], [5]]\ny = [1, 2, 3, 4, 5]\n\n# Split with random_state=42\n",
            "solution_code": "from sklearn.model_selection import train_test_split\n\nX = [[1], [2], [3], [4], [5]]\ny = [1, 2, 3, 4, 5]\n\n# Split with random_state=42\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\nprint(len(X_train))",
            "expected_output": "4",
            "xp": 10
        },
        {
            "id": 104,
            "title": "Linear Regression",
            "order": 2,
            "content": """# 📈 Linear Regression

Predict continuous values:

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

---

## 🎯 Your Task

Train a linear regression on:
- X: `[[1], [2], [3], [4], [5]]`
- y: `[2, 4, 6, 8, 10]` (y = 2x)

Predict for X=6 and print the result.
""",
            "starter_code": "from sklearn.linear_model import LinearRegression\n\nX = [[1], [2], [3], [4], [5]]\ny = [2, 4, 6, 8, 10]\n\n# Train and predict for [[6]]\n",
            "solution_code": "from sklearn.linear_model import LinearRegression\n\nX = [[1], [2], [3], [4], [5]]\ny = [2, 4, 6, 8, 10]\n\n# Train and predict for [[6]]\nmodel = LinearRegression()\nmodel.fit(X, y)\nprediction = model.predict([[6]])\nprint(prediction[0])",
            "expected_output": "12.0",
            "xp": 10
        },
        {
            "id": 105,
            "title": "Model Accuracy",
            "order": 3,
            "content": """# 📊 Model Accuracy

```python
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_true, y_pred)
```

---

## 🎯 Your Task

Calculate accuracy for:
- y_true: `[1, 0, 1, 1, 0]`
- y_pred: `[1, 0, 0, 1, 0]`

Print the result.
""",
            "starter_code": "from sklearn.metrics import accuracy_score\n\ny_true = [1, 0, 1, 1, 0]\ny_pred = [1, 0, 0, 1, 0]\n\n# Calculate accuracy\n",
            "solution_code": "from sklearn.metrics import accuracy_score\n\ny_true = [1, 0, 1, 1, 0]\ny_pred = [1, 0, 0, 1, 0]\n\n# Calculate accuracy\nacc = accuracy_score(y_true, y_pred)\nprint(acc)",
            "expected_output": "0.8",
            "xp": 10
        },
        {
            "id": 106,
            "title": "Classification: K-Nearest Neighbors",
            "order": 4,
            "content": """# 🎯 K-Nearest Neighbors

Classify based on nearest neighbors:

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
```

---

## 🎯 Your Task

Train KNN (k=3) on:
- X: `[[0], [1], [2], [3]]`
- y: `[0, 0, 1, 1]` (0 for first two, 1 for last two)

Predict for X=1.5 and print.
""",
            "starter_code": "from sklearn.neighbors import KNeighborsClassifier\n\nX = [[0], [1], [2], [3]]\ny = [0, 0, 1, 1]\n\n# Train and predict for [[1.5]]\n",
            "solution_code": "from sklearn.neighbors import KNeighborsClassifier\n\nX = [[0], [1], [2], [3]]\ny = [0, 0, 1, 1]\n\n# Train and predict for [[1.5]]\nknn = KNeighborsClassifier(n_neighbors=3)\nknn.fit(X, y)\npred = knn.predict([[1.5]])\nprint(pred[0])",
            "expected_output": "0",
            "xp": 10
        },
        {
            "id": 107,
            "title": "Decision Tree",
            "order": 5,
            "content": """# 🌳 Decision Tree

Use tree-based rules:

```python
from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier()
tree.fit(X, y)
```

---

## 🎯 Your Task

Train a DecisionTree on iris-like data:
- X: `[[1, 2], [1, 4], [4, 2], [4, 4]]`
- y: `[0, 0, 1, 1]`

Predict for `[[2, 3]]` and print.
""",
            "starter_code": "from sklearn.tree import DecisionTreeClassifier\n\nX = [[1, 2], [1, 4], [4, 2], [4, 4]]\ny = [0, 0, 1, 1]\n\n# Train and predict\n",
            "solution_code": "from sklearn.tree import DecisionTreeClassifier\n\nX = [[1, 2], [1, 4], [4, 2], [4, 4]]\ny = [0, 0, 1, 1]\n\n# Train and predict\ntree = DecisionTreeClassifier(random_state=42)\ntree.fit(X, y)\npred = tree.predict([[2, 3]])\nprint(pred[0])",
            "expected_output": "0",
            "xp": 10
        },
        {
            "id": 108,
            "title": "Feature Scaling",
            "order": 6,
            "content": """# ⚖️ Feature Scaling

Normalize features:

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 🎯 Your Task

Scale `[[1, 100], [2, 200], [3, 300]]`.
Print the mean of scaled data (should be ~0).
""",
            "starter_code": "from sklearn.preprocessing import StandardScaler\nimport numpy as np\n\nX = [[1, 100], [2, 200], [3, 300]]\n\n# Scale and print mean\n",
            "solution_code": "from sklearn.preprocessing import StandardScaler\nimport numpy as np\n\nX = [[1, 100], [2, 200], [3, 300]]\n\n# Scale and print mean\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(X)\nprint(round(np.mean(X_scaled), 1))",
            "expected_output": "0.0",
            "xp": 10
        },
        {
            "id": 109,
            "title": "Cross Validation",
            "order": 7,
            "content": """# 🔄 Cross Validation

Evaluate with multiple splits:

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
```

---

## 🎯 Your Task

Use 3-fold CV on LinearRegression with:
- X: `[[1], [2], [3], [4], [5], [6]]`
- y: `[1, 2, 3, 4, 5, 6]`

Print the mean score rounded to 2 decimals.
""",
            "starter_code": "from sklearn.model_selection import cross_val_score\nfrom sklearn.linear_model import LinearRegression\n\nX = [[1], [2], [3], [4], [5], [6]]\ny = [1, 2, 3, 4, 5, 6]\n\n# Cross validation\n",
            "solution_code": "from sklearn.model_selection import cross_val_score\nfrom sklearn.linear_model import LinearRegression\n\nX = [[1], [2], [3], [4], [5], [6]]\ny = [1, 2, 3, 4, 5, 6]\n\n# Cross validation\nmodel = LinearRegression()\nscores = cross_val_score(model, X, y, cv=3)\nprint(round(scores.mean(), 2))",
            "expected_output": "1.0",
            "xp": 10
        },
        {
            "id": 110,
            "title": "Confusion Matrix",
            "order": 8,
            "content": """# 📊 Confusion Matrix

See classification details:

```python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
```

---

## 🎯 Your Task

Calculate confusion matrix for:
- y_true: `[0, 0, 1, 1]`
- y_pred: `[0, 1, 1, 1]`

Print the matrix.
""",
            "starter_code": "from sklearn.metrics import confusion_matrix\n\ny_true = [0, 0, 1, 1]\ny_pred = [0, 1, 1, 1]\n\n# Print confusion matrix\n",
            "solution_code": "from sklearn.metrics import confusion_matrix\n\ny_true = [0, 0, 1, 1]\ny_pred = [0, 1, 1, 1]\n\n# Print confusion matrix\ncm = confusion_matrix(y_true, y_pred)\nprint(cm)",
            "expected_output": "[[1 1]\n [0 2]]",
            "xp": 10
        },
        {
            "id": 111,
            "title": "Making Predictions",
            "order": 9,
            "content": """# 🎯 Complete ML Pipeline

Put it all together!

---

## 🎯 Your Task

Build a complete classifier:
1. Data: X=`[[1], [2], [3], [4]]`, y=`[0, 0, 1, 1]`
2. Train KNeighborsClassifier with k=1
3. Predict for X=2.5
4. Print the prediction
""",
            "starter_code": "from sklearn.neighbors import KNeighborsClassifier\n\nX = [[1], [2], [3], [4]]\ny = [0, 0, 1, 1]\n\n# Complete pipeline\n",
            "solution_code": "from sklearn.neighbors import KNeighborsClassifier\n\nX = [[1], [2], [3], [4]]\ny = [0, 0, 1, 1]\n\n# Complete pipeline\nmodel = KNeighborsClassifier(n_neighbors=1)\nmodel.fit(X, y)\nprediction = model.predict([[2.5]])\nprint(prediction[0])",
            "expected_output": "0",
            "xp": 10
        }
    ]
}
