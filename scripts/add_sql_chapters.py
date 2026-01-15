"""
Script to add SQL Database Design and Advanced Objects chapters.
"""
import json

LESSONS_PATH = "/Users/elijahang/Python-Game-2/frontend/public/data/lessons.json"
COURSE_PATH = "/Users/elijahang/Python-Game-2/frontend/public/data/course-sql-fundamentals.json"

# SQL Database Design lessons (IDs 1300-1308)
SQL_DB_DESIGN_LESSONS = {
    "1300": {
        "id": 1300,
        "title": "CREATE TABLE Basics",
        "content": """# 🏗️ Creating Tables

## What is CREATE TABLE?

`CREATE TABLE` defines a new table with its columns and data types.

## Basic Syntax

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype
);
```

## Example

```sql
CREATE TABLE employees (
    id INTEGER,
    name VARCHAR(100),
    email VARCHAR(255),
    hire_date DATE,
    salary DECIMAL(10, 2)
);
```

## Common Data Types

| Type | Description | Example |
| --- | --- | --- |
| INTEGER | Whole numbers | 42 |
| VARCHAR(n) | Variable text up to n chars | 'Hello' |
| TEXT | Long text | Article content |
| DECIMAL(p,s) | Exact numbers | 99.99 |
| DATE | Date only | 2024-01-15 |
| BOOLEAN | True/False | TRUE |

## Column Order

Columns are created in the order listed.

---

## 🎯 Your Task

Write a CREATE TABLE for `products` with `id` (INTEGER), `name` (VARCHAR(100)), and `price` (DECIMAL(10,2)).
""",
        "starter_code": "-- Create products table\n",
        "solution_code": """-- Create products table
CREATE TABLE products (
    id INTEGER,
    name VARCHAR(100),
    price DECIMAL(10, 2)
);""",
        "expected_output": "Table created successfully",
        "chapter_id": 210,
        "chapter_title": "Database Design"
    },
    "1301": {
        "id": 1301,
        "title": "DROP TABLE",
        "content": """# 🗑️ Deleting Tables with DROP

## What is DROP TABLE?

`DROP TABLE` permanently deletes a table and all its data.

## Syntax

```sql
DROP TABLE table_name;
```

## ⚠️ Warning

This is **irreversible**! All data is lost.

## Safe Dropping

Use `IF EXISTS` to avoid errors if table doesn't exist:

```sql
DROP TABLE IF EXISTS old_table;
```

## When to Use DROP

- Removing temporary tables
- Recreating a table with different structure
- Cleaning up test data

---

## 🎯 Your Task

Write SQL to safely drop a table called `temp_data` using IF EXISTS.
""",
        "starter_code": "-- Drop temp_data safely\n",
        "solution_code": "-- Drop temp_data safely\nDROP TABLE IF EXISTS temp_data;",
        "expected_output": "Table dropped successfully",
        "chapter_id": 210,
        "chapter_title": "Database Design"
    },
    "1302": {
        "id": 1302,
        "title": "ALTER TABLE",
        "content": """# ✏️ Modifying Tables with ALTER

## What is ALTER TABLE?

`ALTER TABLE` changes an existing table's structure.

## Common Operations

### Add a Column

```sql
ALTER TABLE employees
ADD COLUMN phone VARCHAR(20);
```

### Drop a Column

```sql
ALTER TABLE employees
DROP COLUMN phone;
```

### Rename a Column

```sql
ALTER TABLE employees
RENAME COLUMN name TO full_name;
```

### Change Data Type

```sql
ALTER TABLE employees
ALTER COLUMN salary TYPE DECIMAL(12, 2);
```

## Multiple Changes

Some databases allow multiple changes:

```sql
ALTER TABLE products
ADD COLUMN category VARCHAR(50),
ADD COLUMN created_at TIMESTAMP;
```

---

## 🎯 Your Task

Write SQL to add a `description` column (TEXT) to the `products` table.
""",
        "starter_code": "-- Add description column to products\n",
        "solution_code": """-- Add description column to products
ALTER TABLE products
ADD COLUMN description TEXT;""",
        "expected_output": "Table altered successfully",
        "chapter_id": 210,
        "chapter_title": "Database Design"
    },
    "1303": {
        "id": 1303,
        "title": "NOT NULL Constraint",
        "content": """# ❗ NOT NULL: Required Values

## What is NOT NULL?

`NOT NULL` ensures a column cannot be empty.

## Syntax

```sql
CREATE TABLE users (
    id INTEGER NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    nickname VARCHAR(50)  -- This CAN be null
);
```

## Why Use NOT NULL?

- Ensures data completeness
- Prevents accidental empty values
- Makes data queries more predictable

## NOT NULL with INSERT

```sql
-- This works:
INSERT INTO users (id, username, email)
VALUES (1, 'alice', 'alice@email.com');

-- This FAILS (username is required):
INSERT INTO users (id, email)
VALUES (2, 'bob@email.com');
```

## Adding NOT NULL to Existing Column

```sql
ALTER TABLE products
ALTER COLUMN name SET NOT NULL;
```

---

## 🎯 Your Task

Create a `customers` table where `id` and `name` are NOT NULL, but `phone` can be null.
""",
        "starter_code": "-- Create customers table\n",
        "solution_code": """-- Create customers table
CREATE TABLE customers (
    id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20)
);""",
        "expected_output": "Table created successfully",
        "chapter_id": 210,
        "chapter_title": "Database Design"
    },
    "1304": {
        "id": 1304,
        "title": "PRIMARY KEY Constraint",
        "content": """# 🔑 PRIMARY KEY: Unique Identifier

## What is a Primary Key?

A **primary key** uniquely identifies each row.
- Must be unique
- Cannot be NULL
- Only ONE per table

## Syntax

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);
```

## Composite Primary Key

Multiple columns together:

```sql
CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id)
);
```

## Auto-Increment (Common Pattern)

```sql
-- PostgreSQL
id SERIAL PRIMARY KEY

-- MySQL
id INT AUTO_INCREMENT PRIMARY KEY

-- SQLite
id INTEGER PRIMARY KEY AUTOINCREMENT
```

## Why Primary Keys Matter

- Fast lookups
- Relationship references (foreign keys)
- Data integrity

---

## 🎯 Your Task

Create an `orders` table with `id` as PRIMARY KEY and `total` as DECIMAL(10,2).
""",
        "starter_code": "-- Create orders table with primary key\n",
        "solution_code": """-- Create orders table with primary key
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    total DECIMAL(10, 2)
);""",
        "expected_output": "Table created successfully",
        "chapter_id": 210,
        "chapter_title": "Database Design"
    },
    "1305": {
        "id": 1305,
        "title": "FOREIGN KEY Constraint",
        "content": """# 🔗 FOREIGN KEY: Linking Tables

## What is a Foreign Key?

A **foreign key** links one table to another's primary key.

## Syntax

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    total DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

## Why Use Foreign Keys?

1. **Referential integrity**: Can't reference non-existent records
2. **Cascading actions**: Auto-update/delete related records
3. **Documentation**: Shows table relationships

## Cascade Options

```sql
FOREIGN KEY (customer_id) REFERENCES customers(id)
    ON DELETE CASCADE     -- Delete orders when customer deleted
    ON UPDATE CASCADE     -- Update if customer id changes
```

## Visual Example

```
customers (id, name)         orders (id, customer_id, total)
┌────┬───────┐               ┌────┬─────────────┬───────┐
│ id │ name  │     ←─────────│ id │ customer_id │ total │
├────┼───────┤               ├────┼─────────────┼───────┤
│ 1  │ Alice │               │ 1  │ 1           │ 99.99 │
│ 2  │ Bob   │               │ 2  │ 1           │ 50.00 │
└────┴───────┘               └────┴─────────────┴───────┘
```

---

## 🎯 Your Task

Create `order_items` with `order_id` referencing `orders(id)`.
""",
        "starter_code": "-- Create order_items with foreign key\n",
        "solution_code": """-- Create order_items with foreign key
CREATE TABLE order_items (
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);""",
        "expected_output": "Table created successfully",
        "chapter_id": 210,
        "chapter_title": "Database Design"
    },
    "1306": {
        "id": 1306,
        "title": "UNIQUE and CHECK Constraints",
        "content": """# ✅ UNIQUE and CHECK Constraints

## UNIQUE Constraint

Ensures no duplicate values in a column:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email VARCHAR(255) UNIQUE,  -- No duplicate emails!
    username VARCHAR(50) UNIQUE
);
```

## Multiple Columns Unique Together

```sql
CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    UNIQUE (student_id, course_id)  -- Can't enroll twice!
);
```

## CHECK Constraint

Validates data against a condition:

```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2) CHECK (price > 0),
    quantity INTEGER CHECK (quantity >= 0)
);
```

## Multiple Checks

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    age INTEGER CHECK (age >= 18 AND age <= 100),
    salary DECIMAL CHECK (salary >= 0)
);
```

---

## 🎯 Your Task

Create `accounts` table with `email` as UNIQUE and `balance` CHECK >= 0.
""",
        "starter_code": "-- Create accounts with constraints\n",
        "solution_code": """-- Create accounts with constraints
CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    balance DECIMAL(10, 2) CHECK (balance >= 0)
);""",
        "expected_output": "Table created successfully",
        "chapter_id": 210,
        "chapter_title": "Database Design"
    },
    "1307": {
        "id": 1307,
        "title": "DEFAULT Values",
        "content": """# 📝 DEFAULT: Automatic Values

## What is DEFAULT?

`DEFAULT` provides a value when none is specified.

## Syntax

```sql
CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    title VARCHAR(200),
    status VARCHAR(20) DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    view_count INTEGER DEFAULT 0
);
```

## Common Defaults

| Use Case | Example |
| --- | --- |
| Status | `DEFAULT 'active'` |
| Counter | `DEFAULT 0` |
| Timestamp | `DEFAULT CURRENT_TIMESTAMP` |
| Boolean | `DEFAULT TRUE` |

## How INSERT Works

```sql
-- Full insert
INSERT INTO posts (id, title, status)
VALUES (1, 'Hello', 'published');

-- Using defaults
INSERT INTO posts (id, title)
VALUES (2, 'World');
-- status = 'draft', created_at = now, view_count = 0
```

---

## 🎯 Your Task

Create `articles` table with `views` defaulting to 0 and `status` defaulting to 'draft'.
""",
        "starter_code": "-- Create articles with defaults\n",
        "solution_code": """-- Create articles with defaults
CREATE TABLE articles (
    id INTEGER PRIMARY KEY,
    title VARCHAR(200),
    views INTEGER DEFAULT 0,
    status VARCHAR(20) DEFAULT 'draft'
);""",
        "expected_output": "Table created successfully",
        "chapter_id": 210,
        "chapter_title": "Database Design"
    },
    "1308": {
        "id": 1308,
        "title": "Complete Table Design",
        "content": """# 🏆 Putting It All Together

## Real-World Table Design

A well-designed table uses multiple constraints:

```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    sku VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    quantity INTEGER DEFAULT 0 CHECK (quantity >= 0),
    category_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
```

## Design Checklist

✅ Primary key for unique identification
✅ NOT NULL for required fields
✅ UNIQUE for fields that must be distinct
✅ CHECK for data validation
✅ DEFAULT for sensible automatic values
✅ FOREIGN KEY for relationships

## Naming Conventions

- Table names: plural, snake_case (`order_items`)
- Column names: singular, snake_case (`created_at`)
- Primary key: `id` or `table_name_id`
- Foreign key: `referenced_table_id`

---

## 🎯 Your Task

Create a complete `employees` table with proper constraints.
""",
        "starter_code": """-- Create a comprehensive employees table
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    hire_date DATE DEFAULT CURRENT_DATE,
    salary DECIMAL(10, 2) CHECK (salary > 0),
    department_id INTEGER,
    is_active BOOLEAN DEFAULT TRUE
);

SELECT 'Table created successfully' AS result;
""",
        "solution_code": """-- Create a comprehensive employees table
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    hire_date DATE DEFAULT CURRENT_DATE,
    salary DECIMAL(10, 2) CHECK (salary > 0),
    department_id INTEGER,
    is_active BOOLEAN DEFAULT TRUE
);

SELECT 'Table created successfully' AS result;""",
        "expected_output": "Table created successfully",
        "chapter_id": 210,
        "chapter_title": "Database Design"
    }
}

# SQL Advanced Objects lessons (IDs 1320-1327)
SQL_ADVANCED_LESSONS = {
    "1320": {
        "id": 1320,
        "title": "What is a View?",
        "content": """# 👁️ Views: Virtual Tables

## What is a View?

A **view** is a saved query that acts like a virtual table.

## Why Use Views?

1. **Simplify complex queries** - Write once, use many times
2. **Security** - Hide sensitive columns
3. **Abstraction** - Change underlying tables without breaking apps

## Basic Syntax

```sql
CREATE VIEW view_name AS
SELECT columns
FROM table
WHERE condition;
```

## Example

```sql
CREATE VIEW active_customers AS
SELECT id, name, email
FROM customers
WHERE is_active = TRUE;

-- Use like a table:
SELECT * FROM active_customers;
```

## Views Are Updated Automatically

The view always shows current data - it's not a copy!

---

## 🎯 Your Task

Create a view called `recent_orders` selecting orders from the last 30 days.
""",
        "starter_code": "-- Create recent_orders view\n",
        "solution_code": """-- Create recent_orders view
CREATE VIEW recent_orders AS
SELECT *
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL '30 days';""",
        "expected_output": "View created successfully",
        "chapter_id": 211,
        "chapter_title": "Advanced Database Objects"
    },
    "1321": {
        "id": 1321,
        "title": "Creating Complex Views",
        "content": """# 🔧 Advanced Views

## Views with Joins

```sql
CREATE VIEW order_details AS
SELECT 
    o.id AS order_id,
    c.name AS customer_name,
    o.total,
    o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.id;
```

## Views with Aggregations

```sql
CREATE VIEW customer_stats AS
SELECT 
    customer_id,
    COUNT(*) AS order_count,
    SUM(total) AS total_spent,
    AVG(total) AS avg_order
FROM orders
GROUP BY customer_id;
```

## Drop and Replace

```sql
DROP VIEW IF EXISTS my_view;

-- Or recreate:
CREATE OR REPLACE VIEW my_view AS
SELECT ...;
```

## When to Use Views

✅ Frequently used complex queries
✅ Hiding implementation details
✅ Providing consistent data access
❌ Performance-critical queries (can be slow)

---

## 🎯 Your Task

Create a view `product_summary` showing product name and total quantity sold.
""",
        "starter_code": "-- Create product_summary view\n",
        "solution_code": """-- Create product_summary view
CREATE VIEW product_summary AS
SELECT 
    p.name,
    SUM(oi.quantity) AS total_sold
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.name;""",
        "expected_output": "View created successfully",
        "chapter_id": 211,
        "chapter_title": "Advanced Database Objects"
    },
    "1322": {
        "id": 1322,
        "title": "What is an Index?",
        "content": """# ⚡ Indexes: Speed Up Queries

## What is an Index?

An **index** is a data structure that speeds up data retrieval - like a book index!

## Without Index

```
Query: WHERE name = 'Alice'
→ Scan EVERY row (slow for big tables)
```

## With Index

```
Query: WHERE name = 'Alice'
→ Jump directly to matching rows (fast!)
```

## Create an Index

```sql
CREATE INDEX idx_customers_email
ON customers(email);
```

## When Indexes Help

- WHERE clauses: `WHERE email = 'x'`
- JOIN conditions: `ON a.id = b.a_id`
- ORDER BY clauses: `ORDER BY created_at`
- GROUP BY clauses: `GROUP BY category`

## Trade-offs

| Pros | Cons |
| --- | --- |
| Faster reads | Slower writes (INSERT/UPDATE) |
| Quick lookups | Extra storage space |

---

## 🎯 Your Task

Create an index on the `email` column of the `users` table.
""",
        "starter_code": "-- Create email index\n",
        "solution_code": """-- Create email index
CREATE INDEX idx_users_email
ON users(email);""",
        "expected_output": "Index created successfully",
        "chapter_id": 211,
        "chapter_title": "Advanced Database Objects"
    },
    "1323": {
        "id": 1323,
        "title": "Index Best Practices",
        "content": """# 📊 Index Strategies

## Good Index Candidates

1. **Primary key columns** (automatic)
2. **Foreign key columns** (JOIN performance)
3. **Frequently filtered columns**
4. **Columns in ORDER BY**

## Multi-Column Indexes

```sql
-- Good for WHERE first_name AND last_name
CREATE INDEX idx_name
ON employees(first_name, last_name);
```

Order matters! This index helps:
- `WHERE first_name = 'John'` ✅
- `WHERE first_name = 'John' AND last_name = 'Doe'` ✅
- `WHERE last_name = 'Doe'` ❌ (first column not used)

## Unique Indexes

```sql
CREATE UNIQUE INDEX idx_email
ON users(email);
```

Ensures uniqueness AND speeds up lookups!

## Drop an Index

```sql
DROP INDEX idx_name;
```

## Don't Over-Index

- Too many indexes slow down writes
- Index only frequently queried columns
- Monitor query performance

---

## 🎯 Your Task

Create a composite index on `orders(customer_id, order_date)`.
""",
        "starter_code": "-- Create composite index\n",
        "solution_code": """-- Create composite index
CREATE INDEX idx_orders_customer_date
ON orders(customer_id, order_date);""",
        "expected_output": "Index created successfully",
        "chapter_id": 211,
        "chapter_title": "Advanced Database Objects"
    },
    "1324": {
        "id": 1324,
        "title": "SQL Injection Explained",
        "content": """# 🔓 SQL Injection: A Security Threat

## What is SQL Injection?

When user input is directly inserted into SQL, attackers can manipulate queries.

## The Vulnerability

```python
# DANGEROUS CODE - Never do this!
username = request.form['username']
query = f"SELECT * FROM users WHERE username = '{username}'"
```

## The Attack

If user enters: `' OR '1'='1`

Query becomes:
```sql
SELECT * FROM users WHERE username = '' OR '1'='1'
-- Returns ALL users!
```

Even worse: `'; DROP TABLE users; --`
```sql
SELECT * FROM users WHERE username = ''; DROP TABLE users; --'
-- Deletes the entire table!
```

## The Solution: Parameterized Queries

```python
# SAFE - Use placeholders
cursor.execute(
    "SELECT * FROM users WHERE username = ?",
    (username,)
)
```

## Key Takeaways

1. **Never** concatenate user input into SQL
2. **Always** use parameterized queries
3. **Validate** input on the server
4. **Use ORM** when possible (SQLAlchemy, etc.)

---

## 🎯 Your Task

Print understanding of SQL injection prevention.
""",
        "starter_code": "-- SQL injection prevention\nSELECT 'Always use parameterized queries!' AS best_practice;",
        "solution_code": "-- SQL injection prevention\nSELECT 'Always use parameterized queries!' AS best_practice;",
        "expected_output": "Always use parameterized queries!",
        "chapter_id": 211,
        "chapter_title": "Advanced Database Objects"
    }
}

def update_sql_curriculum():
    """Add new SQL lessons"""
    print("Loading lessons.json...")
    with open(LESSONS_PATH, 'r') as f:
        lessons = json.load(f)
    
    print(f"Current lesson count: {len(lessons)}")
    
    # Add SQL Database Design lessons
    for lesson_id, lesson in SQL_DB_DESIGN_LESSONS.items():
        lessons[lesson_id] = lesson
        print(f"  Added lesson {lesson_id}: {lesson['title']}")
    
    # Add SQL Advanced lessons
    for lesson_id, lesson in SQL_ADVANCED_LESSONS.items():
        lessons[lesson_id] = lesson
        print(f"  Added lesson {lesson_id}: {lesson['title']}")
    
    print(f"New lesson count: {len(lessons)}")
    
    with open(LESSONS_PATH, 'w') as f:
        json.dump(lessons, f, indent=2)
    print("✅ lessons.json updated!")

def update_sql_course():
    """Add new chapters to SQL course"""
    print("\nLoading course-sql-fundamentals.json...")
    with open(COURSE_PATH, 'r') as f:
        course = json.load(f)
    
    # Database Design chapter
    db_design_chapter = {
        "id": 210,
        "title": "Database Design",
        "icon": "🏗️",
        "is_boss": False,
        "concepts": [
            {
                "name": "Table Creation",
                "icon": "📊",
                "lessons": [
                    {"id": 1300, "title": "CREATE TABLE Basics", "order": 1},
                    {"id": 1301, "title": "DROP TABLE", "order": 2},
                    {"id": 1302, "title": "ALTER TABLE", "order": 3}
                ]
            },
            {
                "name": "Constraints",
                "icon": "🔒",
                "lessons": [
                    {"id": 1303, "title": "NOT NULL Constraint", "order": 4},
                    {"id": 1304, "title": "PRIMARY KEY Constraint", "order": 5},
                    {"id": 1305, "title": "FOREIGN KEY Constraint", "order": 6},
                    {"id": 1306, "title": "UNIQUE and CHECK Constraints", "order": 7},
                    {"id": 1307, "title": "DEFAULT Values", "order": 8},
                    {"id": 1308, "title": "Complete Table Design", "order": 9}
                ]
            }
        ]
    }
    
    # Advanced Objects chapter
    advanced_chapter = {
        "id": 211,
        "title": "Advanced Database Objects",
        "icon": "⚙️",
        "is_boss": False,
        "concepts": [
            {
                "name": "Views",
                "icon": "👁️",
                "lessons": [
                    {"id": 1320, "title": "What is a View?", "order": 1},
                    {"id": 1321, "title": "Creating Complex Views", "order": 2}
                ]
            },
            {
                "name": "Indexes & Security",
                "icon": "⚡",
                "lessons": [
                    {"id": 1322, "title": "What is an Index?", "order": 3},
                    {"id": 1323, "title": "Index Best Practices", "order": 4},
                    {"id": 1324, "title": "SQL Injection Explained", "order": 5}
                ]
            }
        ]
    }
    
    existing_ids = [ch["id"] for ch in course["chapters"]]
    
    if 210 not in existing_ids:
        course["chapters"].append(db_design_chapter)
        print("  Added Database Design chapter (210)")
    
    if 211 not in existing_ids:
        course["chapters"].append(advanced_chapter)
        print("  Added Advanced Database Objects chapter (211)")
    
    with open(COURSE_PATH, 'w') as f:
        json.dump(course, f, indent=2)
    print("✅ course-sql-fundamentals.json updated!")

if __name__ == "__main__":
    print("🚀 Adding SQL curriculum chapters...")
    update_sql_curriculum()
    update_sql_course()
    print("\n✨ Done! SQL Database Design and Advanced Objects added.")
