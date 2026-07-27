# 🧰 Modules & Libraries (Basics)

Modules and Libraries provide **ready-made code** that we can use in our programs instead of writing everything from scratch.

---

# 📦 Module

## Definition

A **Module** is a **Python file (`.py`)** that contains **functions, classes, and variables**.

### Examples

- `math`
- `random`
- `datetime`
- `os`

### Purpose

- Reuse existing code
- Reduce coding time
- Keep programs organized

---

# 📚 Library

## Definition

A **Library** is a **collection of multiple modules**.

### Purpose

- Provides ready-made tools for different tasks
- Makes programming faster and easier

---

# 🔄 Difference Between Module and Library

| Module | Library |
|---------|----------|
| A single Python file (`.py`) | Collection of multiple modules |
| Contains functions, classes, variables | Contains related modules |
| Example: `math` | Example: Python Standard Library |

---

# 📥 Importing Modules

Before using a module, it must be **imported**.

---

## Method 1 — Import Entire Module

### Syntax

```python
import module_name
```

### Example

```python
import math

print(math.sqrt(25))
```

### Purpose

Import the **entire module** and access its functions using **dot (`.`) notation**.

---

## Method 2 — Import Specific Function

### Syntax

```python
from module_name import function_name
```

### Example

```python
from math import sqrt

print(sqrt(25))
```

### Purpose

Import **only the required function**, so there is no need to write the module name every time.

---

# 📊 Difference Between `import` and `from ... import ...`

| import | from ... import ... |
|---------|----------------------|
| Imports the complete module | Imports only required functions/classes |
| Access using `module.function()` | Access function directly |
| Example: `math.sqrt(25)` | Example: `sqrt(25)` |
