#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache defines a MRU caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    print("DISCARD:", self.mru_key)
                    del self.cache_data[self.mru_key]
                self.cache_data[key] = item
            self.mru_key = key

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.mru_key = key
            return self.cache_data[key]
        return None
