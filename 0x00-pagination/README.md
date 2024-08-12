**0x00. Pagination**

---

Back-end  
Weight: 1  
Project over - took place from May 16, 2024 6:00 AM to May 21, 2024 6:00 AM

**Resources**  
Read or watch:
- REST API Design: Pagination
- HATEOAS

**Learning Objectives**  
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

**Requirements**
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word; it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

**Setup**  
`Popular_Baby_Names.csv`  
Use this data file for your project.

**Tasks**  
1. **Simple helper function**  
   Write a function named `index_range` that takes two integer arguments `page` and `page_size`. The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters. Page numbers are 1-indexed, i.e., the first page is page 1.

   - **File:** `0-simple_helper_function.py`

2. **Simple pagination**  
   Copy `index_range` from the previous task and the following class into your code:

   ```python
   import csv
   from typing import List

   class Server:
       """Server class to paginate a database of popular baby names."""
       DATA_FILE = "Popular_Baby_Names.csv"

       def __init__(self):
           self.__dataset = None

       def dataset(self) -> List[List]:
           """Cached dataset"""
           if self.__dataset is None:
               with open(self.DATA_FILE) as f:
                   reader = csv.reader(f)
                   dataset = [row for row in reader]
               self.__dataset = dataset[1:]

           return self.__dataset

       def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
           pass
   ```
   Implement a method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10. Use `index_range` to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e., the correct list of rows). If the input arguments are out of range for the dataset, an empty list should be returned.

   - **File:** `1-simple_pagination.py`

3. **Hypermedia pagination**  
   Replicate code from the previous task. Implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the following key-value pairs:
   - `page_size`: the length of the returned dataset page
   - `page`: the current page number
   - `data`: the dataset page (equivalent to return from previous task)
   - `next_page`: number of the next page, None if no next page
   - `prev_page`: number of the previous page, None if no previous page
   - `total_pages`: the total number of pages in the dataset as an integer

   Make sure to reuse `get_page` in your implementation.

   - **File:** `2-hypermedia_pagination.py`

4. **Deletion-resilient hypermedia pagination**  
   Implement a `get_hyper_index` method with two integer arguments: `index` with a None default value and `page_size` with a default value of 10. The method should return a dictionary with the following key-value pairs:
   - `index`: the current start index of the return page.
   - `next_index`: the next index to query with.
   - `page_size`: the current page size
   - `data`: the actual page of the dataset

   Use assert to verify that index is in a valid range. The method should handle cases where rows are deleted from the dataset.

   - **File:** `3-hypermedia_del_pagination.py`
