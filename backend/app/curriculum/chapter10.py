# Chapter 10: Algorithms
CHAPTER_10 = {
    "id": 11,
    "title": "Algorithms",
    "slug": "python-algorithms",
    "icon": "🧮",
    "is_boss": False,
    "lessons": [
        {
            "id": 85,
            "title": "Linear Search",
            "order": 1,
            "content": """# 🔍 Linear Search

Check each element until found:

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

---

## 🎯 Your Task

Given: `numbers = [5, 2, 8, 1, 9]`
Search for `8` and print its index.
""",
            "starter_code": "numbers = [5, 2, 8, 1, 9]\ntarget = 8\n\n# Find index of target\n",
            "solution_code": "numbers = [5, 2, 8, 1, 9]\ntarget = 8\n\n# Find index of target\nfor i, val in enumerate(numbers):\n    if val == target:\n        print(i)\n        break",
            "expected_output": "2",
            "xp": 10
        },
        {
            "id": 86,
            "title": "Binary Search",
            "order": 2,
            "content": """# 🔍 Binary Search

For sorted arrays, divide and conquer:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

## 🎯 Your Task

Given: `sorted_nums = [1, 3, 5, 7, 9, 11, 13]`
Find index of `7` using binary search and print it.
""",
            "starter_code": "sorted_nums = [1, 3, 5, 7, 9, 11, 13]\ntarget = 7\n\nleft, right = 0, len(sorted_nums) - 1\nresult = -1\n\n# Binary search\n",
            "solution_code": "sorted_nums = [1, 3, 5, 7, 9, 11, 13]\ntarget = 7\n\nleft, right = 0, len(sorted_nums) - 1\nresult = -1\n\n# Binary search\nwhile left <= right:\n    mid = (left + right) // 2\n    if sorted_nums[mid] == target:\n        result = mid\n        break\n    elif sorted_nums[mid] < target:\n        left = mid + 1\n    else:\n        right = mid - 1\n\nprint(result)",
            "expected_output": "3",
            "xp": 10
        },
        {
            "id": 87,
            "title": "Bubble Sort",
            "order": 3,
            "content": """# 🫧 Bubble Sort

Swap adjacent elements if out of order:

```python
for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

---

## 🎯 Your Task

Sort `[64, 34, 25, 12, 22]` using bubble sort.
Print the sorted list.
""",
            "starter_code": "arr = [64, 34, 25, 12, 22]\n\n# Bubble sort\n\n\n# Print sorted array\n",
            "solution_code": "arr = [64, 34, 25, 12, 22]\n\n# Bubble sort\nfor i in range(len(arr)):\n    for j in range(len(arr) - 1):\n        if arr[j] > arr[j + 1]:\n            arr[j], arr[j + 1] = arr[j + 1], arr[j]\n\n# Print sorted array\nprint(arr)",
            "expected_output": "[12, 22, 25, 34, 64]",
            "xp": 10
        },
        {
            "id": 88,
            "title": "Find Maximum",
            "order": 4,
            "content": """# 🔝 Finding Maximum

```python
max_val = arr[0]
for val in arr:
    if val > max_val:
        max_val = val
```

---

## 🎯 Your Task

Find the maximum in `[3, 7, 2, 9, 4, 1]`.
Print the result.
""",
            "starter_code": "numbers = [3, 7, 2, 9, 4, 1]\n\n# Find maximum\n",
            "solution_code": "numbers = [3, 7, 2, 9, 4, 1]\n\n# Find maximum\nmax_val = numbers[0]\nfor num in numbers:\n    if num > max_val:\n        max_val = num\n\nprint(max_val)",
            "expected_output": "9",
            "xp": 10
        },
        {
            "id": 89,
            "title": "Count Occurrences",
            "order": 5,
            "content": """# 📊 Counting

```python
count = 0
for val in arr:
    if val == target:
        count += 1
```

---

## 🎯 Your Task

Count how many times `5` appears in `[5, 3, 5, 1, 5, 2]`.
Print the count.
""",
            "starter_code": "numbers = [5, 3, 5, 1, 5, 2]\ntarget = 5\n\n# Count occurrences\n",
            "solution_code": "numbers = [5, 3, 5, 1, 5, 2]\ntarget = 5\n\n# Count occurrences\ncount = 0\nfor num in numbers:\n    if num == target:\n        count += 1\n\nprint(count)",
            "expected_output": "3",
            "xp": 10
        },
        {
            "id": 90,
            "title": "Reverse Array",
            "order": 6,
            "content": """# 🔄 Reversing

```python
reversed_arr = arr[::-1]
# Or in-place: arr.reverse()
```

---

## 🎯 Your Task

Reverse `[1, 2, 3, 4, 5]` and print the result.
""",
            "starter_code": "arr = [1, 2, 3, 4, 5]\n\n# Reverse and print\n",
            "solution_code": "arr = [1, 2, 3, 4, 5]\n\n# Reverse and print\nprint(arr[::-1])",
            "expected_output": "[5, 4, 3, 2, 1]",
            "xp": 10
        },
        {
            "id": 91,
            "title": "Remove Duplicates",
            "order": 7,
            "content": """# 🧹 Remove Duplicates

```python
unique = list(set(arr))
```

---

## 🎯 Your Task

Remove duplicates from `[1, 2, 2, 3, 3, 3, 4]`.
Print sorted unique values.
""",
            "starter_code": "arr = [1, 2, 2, 3, 3, 3, 4]\n\n# Remove duplicates and sort\n",
            "solution_code": "arr = [1, 2, 2, 3, 3, 3, 4]\n\n# Remove duplicates and sort\nunique = sorted(set(arr))\nprint(unique)",
            "expected_output": "[1, 2, 3, 4]",
            "xp": 10
        },
        {
            "id": 92,
            "title": "Two Sum",
            "order": 8,
            "content": """# 🎯 Two Sum Problem

Find two numbers that sum to a target.

---

## 🎯 Your Task

Given: `nums = [2, 7, 11, 15]`, `target = 9`
Find two numbers that add to 9 and print them.
""",
            "starter_code": "nums = [2, 7, 11, 15]\ntarget = 9\n\n# Find two numbers that sum to target\n",
            "solution_code": "nums = [2, 7, 11, 15]\ntarget = 9\n\n# Find two numbers that sum to target\nfor i in range(len(nums)):\n    for j in range(i + 1, len(nums)):\n        if nums[i] + nums[j] == target:\n            print(nums[i], nums[j])",
            "expected_output": "2 7",
            "xp": 10
        },
        {
            "id": 93,
            "title": "Fibonacci",
            "order": 9,
            "content": """# 🌀 Fibonacci Sequence

Each number is sum of previous two: 0, 1, 1, 2, 3, 5, 8...

---

## 🎯 Your Task

Generate first 8 Fibonacci numbers and print them.
""",
            "starter_code": "# Generate first 8 Fibonacci numbers\n",
            "solution_code": "# Generate first 8 Fibonacci numbers\nfib = [0, 1]\nfor i in range(6):\n    fib.append(fib[-1] + fib[-2])\n\nprint(fib)",
            "expected_output": "[0, 1, 1, 2, 3, 5, 8, 13]",
            "xp": 10
        }
    ]
}
