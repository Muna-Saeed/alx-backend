# Caching system project:

# Caching System

This project implements various caching mechanisms in Python by extending a base caching class. The caching strategies implemented include:

1. **Basic Cache (No limit)**
2. **FIFO Cache (First In First Out)**
3. **LIFO Cache (Last In First Out)**
4. **LRU Cache (Least Recently Used)**
5. **MRU Cache (Most Recently Used)**
6. **LFU Cache (Least Frequently Used)**

## Requirements

- Python 3.x
- Basic knowledge of classes and inheritance in Python

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/Muna-Saeed/alx-backend.git
```

Navigate to the project directory:

```bash
cd alx-backend/0x01-caching
```

## Usage

### Basic Cache

```python
from 0-basic_cache import BasicCache

my_cache = BasicCache()
my_cache.put("A", "Hello")
print(my_cache.get("A"))  # Output: Hello
```

### FIFO Cache

```python
from 1-fifo_cache import FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.put("E", "Battery")  # This will discard "A" since it's FIFO
print(my_cache.get("A"))  # Output: None
```

### LIFO Cache

```python
from 2-lifo_cache import LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.put("E", "Battery")  # This will discard "D" since it's LIFO
print(my_cache.get("D"))  # Output: None
```

### LRU Cache

```python
from 3-lru_cache import LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.put("E", "Battery")  # This will discard "A" since it's LRU
print(my_cache.get("A"))  # Output: None
```

### MRU Cache

```python
from 4-mru_cache import MRUCache

my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.put("E", "Battery")  # This will discard "D" since it's MRU
print(my_cache.get("D"))  # Output: None
```

### LFU Cache

```python
from 100-lfu_cache import LFUCache

my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.put("E", "Battery")  # This will discard "A" since it's LFU
print(my_cache.get("A"))  # Output: None
```

## Project Structure

```plaintext
0x01-caching/
├── base_caching.py
├── 0-basic_cache.py
├── 1-fifo_cache.py
├── 2-lifo_cache.py
├── 3-lru_cache.py
├── 4-mru_cache.py
├── 100-lfu_cache.py
├── 0-main.py
├── 1-main.py
├── 2-main.py
├── 3-main.py
├── 4-main.py
├── 100-main.py
└── README.md
```

## Author

[Muna Saeed](https://github.com/alx-backend/0x01-caching/Muna-Saeed)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
