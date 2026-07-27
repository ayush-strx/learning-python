# 📁 OS Module

The **os** module is a built-in Python module used to **interact with the Operating System**.

Before using it, import the module.

```python
import os
```

---

# 📖 Common OS Functions

## 1. `getcwd()`

### Definition

Returns the **current working directory**.

### Syntax

```python
os.getcwd()
```

### Purpose

Display the current folder where the Python program is running.

### Example

```python
import os

print(os.getcwd())
```

Possible Output

```text
C:\Users\Ayush\Documents\Python
```

---

## 2. `listdir()`

### Definition

Returns a list of all files and folders in the current directory.

### Syntax

```python
os.listdir()
```

### Purpose

Display all files and folders in the current directory.

### Example

```python
import os

print(os.listdir())
```

Possible Output

```text
['main.py', 'notes.txt', 'Projects']
```

---

## 3. `mkdir()`

### Definition

Creates a new folder (directory).

### Syntax

```python
os.mkdir("FolderName")
```

### Purpose

Create a new directory.

### Example

```python
import os

os.mkdir("Python")
```

---

## 4. `rename()`

### Definition

Renames a file or folder.

### Syntax

```python
os.rename("old_name", "new_name")
```

### Purpose

Change the name of a file or folder.

### Example

```python
import os

os.rename("Python", "PythonNotes")
```

---

## 5. `remove()`

### Definition

Deletes a file.

### Syntax

```python
os.remove("filename")
```

### Purpose

Delete a file from the current directory.

### Example

```python
import os

os.remove("demo.txt")
```

> **Note:** `remove()` deletes **only files**, not folders.

---

# 📊 OS Module Functions

| Function | Purpose |
|----------|---------|
| `getcwd()` | Get the current working directory |
| `listdir()` | Display all files and folders |
| `mkdir()` | Create a new folder |
| `rename()` | Rename a file or folder |
| `remove()` | Delete a file |
