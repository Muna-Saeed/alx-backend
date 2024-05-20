# alx-backend

# Pagination Project

This project involves creating a paginated dataset using Python. You will learn how to paginate datasets using simple parameters, hypermedia metadata, and ensure pagination is resilient to deletions.

## Resources

Read or watch:
- [REST API Design: Pagination](https://restfulapi.net/rest-api-design-pagination/)
- [HATEOAS](https://restfulapi.net/hateoas/)

## Learning Objectives

By the end of this project, you should be able to explain:
- How to paginate a dataset with simple `page` and `page_size` parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Documentation should be a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated

## Setup

Use the `Popular_Baby_Names.csv` data file for your project. This file contains the dataset you will use to implement pagination.

## Project Structure

```
project_folder/
├── README.md
├── main.py
├── pagination.py
├── Popular_Baby_Names.csv
└── tests/
    └── test_pagination.py
```

## Instructions

1. **Dataset Preparation:**
   - Load the `Popular_Baby_Names.csv` file.
   - Implement functions to paginate the dataset.

2. **Simple Pagination:**
   - Implement pagination using `page` and `page_size` parameters.
   - Ensure the implementation is efficient and handles edge cases.

3. **Hypermedia Pagination:**
   - Implement pagination with hypermedia metadata.
   - Include links for `next`, `previous`, `first`, and `last` pages.

4. **Deletion-Resilient Pagination:**
   - Ensure that pagination remains consistent even if items are deleted from the dataset.
   - Implement necessary logic to handle gaps created by deletions.

5. **Documentation:**
   - Document all modules, classes, and functions.
   - Ensure all code is type-annotated.

6. **Testing:**
   - Write unit tests to verify the functionality of your pagination.
   - Ensure all edge cases are covered.

## Example Functions

### Pagination with Page and Page Size

```python
def paginate(data: List[Dict], page: int, page_size: int) -> Dict:
    """
    Paginates the dataset.
    
    Args:
    data (List[Dict]): The dataset to paginate.
    page (int): The page number.
    page_size (int): The number of items per page.
    
    Returns:
    Dict: A dictionary with paginated data and metadata.
    """
    pass
```

### Hypermedia Pagination

```python
def paginate_hypermedia(data: List[Dict], page: int, page_size: int) -> Dict:
    """
    Paginates the dataset with hypermedia metadata.
    
    Args:
    data (List[Dict]): The dataset to paginate.
    page (int): The page number.
    page_size (int): The number of items per page.
    
    Returns:
    Dict: A dictionary with paginated data and hypermedia links.
    """
    pass
```

### Deletion-Resilient Pagination

```python
def paginate_resilient(data: List[Dict], page: int, page_size: int) -> Dict:
    """
    Paginates the dataset in a deletion-resilient manner.
    
    Args:
    data (List[Dict]): The dataset to paginate.
    page (int): The page number.
    page_size (int): The number of items per page.
    
    Returns:
    Dict: A dictionary with paginated data and metadata.
    """
    pass
```

## Testing

Use the `tests/test_pagination.py` file to write your unit tests. Ensure you cover various scenarios including edge cases.

```python
import unittest
from pagination import paginate, paginate_hypermedia, paginate_resilient

class TestPagination(unittest.TestCase):

    def setUp(self):
        self.data = load_data('Popular_Baby_Names.csv')

    def test_paginate(self):
        result = paginate(self.data, page=1, page_size=10)
        self.assertEqual(len(result['data']), 10)
        self.assertIn('page', result)
        self.assertIn('page_size', result)

    def test_paginate_hypermedia(self):
        result = paginate_hypermedia(self.data, page=1, page_size=10)
        self.assertIn('next', result)
        self.assertIn('previous', result)

    def test_paginate_resilient(self):
        result = paginate_resilient(self.data, page=1, page_size=10)
        self.assertEqual(len(result['data']), 10)

if __name__ == '__main__':
    unittest.main()
```

## Conclusion

By completing this project, you will gain hands-on experience in implementing various pagination strategies, ensuring data consistency, and writing comprehensive documentation and tests.
