# Chapter 10: Algorithms
# Enhanced with full detailed definitions and explanations

CHAPTER_10 = {
    "id": 12,
    "title": "Algorithms",
    "slug": "python-algorithms",
    "icon": "🧮",
    "is_boss": False,
    "lessons": [
        {
            "id": 86,
            "title": "Linear Search",
            "order": 1,
            "content": """# 🔍 Linear Search

## What is an Algorithm?

An **algorithm** is a step-by-step procedure for solving a problem. It's like a recipe - specific instructions to achieve a result.

## Linear Search: The Simplest Search

Check each element one by one until you find what you're looking for:

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i  # Found! Return index
    return -1  # Not found
```

## How It Works (Step by Step)

Searching for `8` in `[5, 2, 8, 1, 9]`:

| Step | Check | Match? | Action |
| --- | --- | --- | --- |
| 1 | 5 | No | Continue |
| 2 | 2 | No | Continue |
| 3 | 8 | **Yes!** | Return index 2 |

## Time Complexity

- **Best case**: O(1) - target is first element
- **Worst case**: O(n) - target is last or not found
- **Average**: O(n/2) → O(n)

Linear search is simple but slow for large datasets.

---

## 🎯 Your Task

Search for `8` in `[5, 2, 8, 1, 9]` and print its index.
""",
            "starter_code": "numbers = [5, 2, 8, 1, 9]\ntarget = 8\n\n# Find index of target\n",
            "solution_code": "numbers = [5, 2, 8, 1, 9]\ntarget = 8\n\n# Find index of target\nfor i, val in enumerate(numbers):\n    if val == target:\n        print(i)\n        break",
            "expected_output": "2",
            "xp": 10
        },
        {
            "id": 87,
            "title": "Binary Search",
            "order": 2,
            "content": """# 🔍 Binary Search

## The Divide and Conquer Approach

For **sorted arrays**, binary search is much faster:

1. Look at the middle element
2. If it's the target, done!
3. If target is smaller, search left half
4. If target is larger, search right half
5. Repeat until found or range is empty

## The Algorithm

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Not found
```

## Example: Finding 7

Array: `[1, 3, 5, 7, 9, 11, 13]`

| Step | Left | Right | Mid | arr[mid] | Action |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 6 | 3 | 7 | Found! |

## Time Complexity: O(log n)

With each step, we eliminate half the remaining elements!
- 1000 items → ~10 steps
- 1,000,000 items → ~20 steps

---

## 🎯 Your Task

Use binary search to find index of `7` in `[1, 3, 5, 7, 9, 11, 13]`.
""",
            "starter_code": "sorted_nums = [1, 3, 5, 7, 9, 11, 13]\ntarget = 7\n\nleft, right = 0, len(sorted_nums) - 1\nresult = -1\n\n# Binary search\n",
            "solution_code": "sorted_nums = [1, 3, 5, 7, 9, 11, 13]\ntarget = 7\n\nleft, right = 0, len(sorted_nums) - 1\nresult = -1\n\n# Binary search\nwhile left <= right:\n    mid = (left + right) // 2\n    if sorted_nums[mid] == target:\n        result = mid\n        break\n    elif sorted_nums[mid] < target:\n        left = mid + 1\n    else:\n        right = mid - 1\n\nprint(result)",
            "expected_output": "3",
            "xp": 10
        },
        {
            "id": 88,
            "title": "Bubble Sort",
            "order": 3,
            "content": """# 🫧 Bubble Sort

## How Bubble Sort Works

Compare adjacent elements and swap if out of order. Larger values "bubble up" to the end.

## The Algorithm

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

## Visualization

Sorting `[64, 34, 25]`:

**Pass 1:**
- Compare 64, 34 → swap → `[34, 64, 25]`
- Compare 64, 25 → swap → `[34, 25, 64]`

**Pass 2:**
- Compare 34, 25 → swap → `[25, 34, 64]`
- Compare 34, 64 → no swap

**Result:** `[25, 34, 64]` ✓

## Time Complexity

- **Always**: O(n²) - compares every pair
- **Not efficient** for large datasets
- But easy to understand and implement!

## Why "Bubble"?

Each pass, the largest unsorted element "bubbles up" to its correct position.

---

## 🎯 Your Task

Sort `[64, 34, 25, 12, 22]` using bubble sort and print the result.
""",
            "starter_code": "arr = [64, 34, 25, 12, 22]\n\n# Bubble sort\n\n\n# Print sorted array\n",
            "solution_code": "arr = [64, 34, 25, 12, 22]\n\n# Bubble sort\nfor i in range(len(arr)):\n    for j in range(len(arr) - 1):\n        if arr[j] > arr[j + 1]:\n            arr[j], arr[j + 1] = arr[j + 1], arr[j]\n\n# Print sorted array\nprint(arr)",
            "expected_output": "[12, 22, 25, 34, 64]",
            "xp": 10
        },
        {
            "id": 89,
            "title": "Find Maximum",
            "order": 4,
            "content": """# 🔝 Finding the Maximum Value

## The Algorithm

Track the largest value seen so far:

```python
def find_max(arr):
    max_val = arr[0]  # Assume first is largest
    
    for val in arr:
        if val > max_val:
            max_val = val  # Found a larger one!
    
    return max_val
```

## Step by Step

Finding max in `[3, 7, 2, 9, 4]`:

| Step | Current | max_val | Action |
| --- | --- | --- | --- |
| 1 | 3 | 3 | Initialize |
| 2 | 7 | 7 | Update (7 > 3) |
| 3 | 2 | 7 | No change |
| 4 | 9 | 9 | Update (9 > 7) |
| 5 | 4 | 9 | No change |

**Result:** 9

## Python's Built-in

```python
max([3, 7, 2, 9, 4])  # 9
min([3, 7, 2, 9, 4])  # 2
```

## Time Complexity: O(n)

Must check every element at least once.

---

## 🎯 Your Task

Find the maximum value in `[3, 7, 2, 9, 4, 1]` and print it.
""",
            "starter_code": "numbers = [3, 7, 2, 9, 4, 1]\n\n# Find maximum\n",
            "solution_code": "numbers = [3, 7, 2, 9, 4, 1]\n\n# Find maximum\nmax_val = numbers[0]\nfor num in numbers:\n    if num > max_val:\n        max_val = num\n\nprint(max_val)",
            "expected_output": "9",
            "xp": 10
        },
        {
            "id": 90,
            "title": "Count Occurrences",
            "order": 5,
            "content": """# 📊 Counting Occurrences

## The Problem

How many times does a value appear in a list?

## The Algorithm

```python
def count_occurrences(arr, target):
    count = 0
    for val in arr:
        if val == target:
            count += 1
    return count
```

## Step by Step Example

Counting `5` in `[5, 3, 5, 1, 5, 2]`:

| Element | Match? | Count |
| --- | --- | --- |
| 5 | ✓ | 1 |
| 3 | ✗ | 1 |
| 5 | ✓ | 2 |
| 1 | ✗ | 2 |
| 5 | ✓ | 3 |
| 2 | ✗ | 3 |

**Result:** 3

## Python's Built-in

```python
[5, 3, 5, 1, 5, 2].count(5)  # 3
```

## Use Cases

- Count word frequency in text
- Count votes for candidates
- Find most common element

---

## 🎯 Your Task

Count how many times `5` appears in `[5, 3, 5, 1, 5, 2]` and print the count.
""",
            "starter_code": "numbers = [5, 3, 5, 1, 5, 2]\ntarget = 5\n\n# Count occurrences\n",
            "solution_code": "numbers = [5, 3, 5, 1, 5, 2]\ntarget = 5\n\n# Count occurrences\ncount = 0\nfor num in numbers:\n    if num == target:\n        count += 1\n\nprint(count)",
            "expected_output": "3",
            "xp": 10
        },
        {
            "id": 91,
            "title": "Reverse Array",
            "order": 6,
            "content": """# 🔄 Reversing an Array

## Multiple Approaches

### 1. Slicing (Pythonic)
```python
reversed_arr = arr[::-1]
```

### 2. Built-in reverse (in-place)
```python
arr.reverse()  # Modifies original
```

### 3. Built-in reversed (new iterator)
```python
list(reversed(arr))
```

### 4. Manual (two pointers)
```python
def reverse(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

## Understanding Slicing

`arr[start:stop:step]`
- `[::-1]` means: start at end, go to beginning, step -1

## Time Complexity

All methods: O(n) - must touch every element

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
            "id": 92,
            "title": "Remove Duplicates",
            "order": 7,
            "content": """# 🧹 Removing Duplicates

## Using Set

The easiest way - sets automatically remove duplicates:

```python
arr = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(arr))  # [1, 2, 3, 4]
```

⚠️ **Warning**: Sets don't preserve order!

## Preserving Order

```python
def remove_duplicates_ordered(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```

## Using dict.fromkeys() (Python 3.7+)

```python
list(dict.fromkeys([1, 2, 2, 3, 3]))  # [1, 2, 3]
```

## Use Cases

- Clean user input
- Prepare data for analysis
- Remove redundant items

---

## 🎯 Your Task

Remove duplicates from `[1, 2, 2, 3, 3, 3, 4]` and print the sorted unique values.
""",
            "starter_code": "arr = [1, 2, 2, 3, 3, 3, 4]\n\n# Remove duplicates and sort\n",
            "solution_code": "arr = [1, 2, 2, 3, 3, 3, 4]\n\n# Remove duplicates and sort\nunique = sorted(set(arr))\nprint(unique)",
            "expected_output": "[1, 2, 3, 4]",
            "xp": 10
        },
        {
            "id": 93,
            "title": "Two Sum",
            "order": 8,
            "content": """# 🎯 The Two Sum Problem

## The Problem

Find two numbers in an array that add up to a target sum.

## Brute Force Approach

Check every pair:

```python
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return None
```

**Time Complexity**: O(n²)

## Optimized Approach (Hash Map)

```python
def two_sum_fast(nums, target):
    seen = {}
    for num in nums:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen[num] = True
    return None
```

**Time Complexity**: O(n)

## Why This is Famous

This is **THE** most common coding interview question! It teaches:
- Hash tables
- Trade-offs between time and space
- Problem-solving strategies

---

## 🎯 Your Task

Find two numbers in `[2, 7, 11, 15]` that add up to 9 and print them.
""",
            "starter_code": "nums = [2, 7, 11, 15]\ntarget = 9\n\n# Find two numbers that sum to target\n",
            "solution_code": "nums = [2, 7, 11, 15]\ntarget = 9\n\n# Find two numbers that sum to target\nfor i in range(len(nums)):\n    for j in range(i + 1, len(nums)):\n        if nums[i] + nums[j] == target:\n            print(nums[i], nums[j])",
            "expected_output": "2 7",
            "xp": 10
        },
        {
            "id": 94,
            "title": "Fibonacci",
            "order": 9,
            "content": """# 🌀 Fibonacci Sequence

## The Pattern

Each number is the sum of the two before it:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2)

## Iterative Approach

```python
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]
```

## Recursive Approach

```python
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)
```

⚠️ Recursive is elegant but slow (O(2^n)) without memoization!

## Where Fibonacci Appears

- Nature: flower petals, pinecones, shells
- Art: golden ratio
- Computer science: algorithm analysis
- Finance: Fibonacci retracements

---

## 🎯 Your Task

Generate the first 8 Fibonacci numbers and print them.
""",
            "starter_code": "# Generate first 8 Fibonacci numbers\n",
            "solution_code": "# Generate first 8 Fibonacci numbers\nfib = [0, 1]\nfor i in range(6):\n    fib.append(fib[-1] + fib[-2])\n\nprint(fib)",
            "expected_output": "[0, 1, 1, 2, 3, 5, 8, 13]",
            "xp": 10
        }
    ]
}
