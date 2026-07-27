# 📅 Datetime Module

The **datetime** module is a built-in Python module used to work with **dates and time**.

Before using it, import the module.

```python
import datetime
```

---

# 📖 Common Datetime Functions

## 1. `datetime.now()`

### Definition

Returns the **current date and current time**.

### Syntax

```python
datetime.datetime.now()
```

### Purpose

Get the current system date and time.

### Example

```python
import datetime

print(datetime.datetime.now())
```

Possible Output

```text
2026-07-28 10:45:12.123456
```

---

## 2. `date.today()`

### Definition

Returns the **current date**.

### Syntax

```python
datetime.date.today()
```

### Purpose

Get today's date.

### Example

```python
import datetime

print(datetime.date.today())
```

Output

```text
2026-07-28
```

---

## 3. `strftime()`

### Definition

Formats a date or time into a readable string.

### Syntax

```python
date.strftime(format)
```

### Purpose

Display date and time in different formats.

### Example

```python
import datetime

today = datetime.datetime.now()

print(today.strftime("%d-%m-%Y"))
```

Output

```text
28-07-2026
```

### Common Format Codes

| Code | Meaning | Example |
|------|---------|---------|
| `%d` | Day | 28 |
| `%m` | Month | 07 |
| `%Y` | Year | 2026 |
| `%H` | Hour (24-hour) | 15 |
| `%M` | Minute | 30 |
| `%S` | Second | 45 |

---

## 4. `date()`

### Definition

Creates a specific date.

### Syntax

```python
datetime.date(year, month, day)
```

### Purpose

Create a custom date.

### Example

```python
import datetime

date = datetime.date(2026, 7, 28)

print(date)
```

Output

```text
2026-07-28
```

---

# 📊 Datetime Module Functions

| Function | Purpose |
|----------|---------|
| `datetime.now()` | Get current date and time |
| `date.today()` | Get today's date |
| `strftime()` | Format date and time |
| `date(year, month, day)` | Create a specific date |
