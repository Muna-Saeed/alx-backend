#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFUCache defines a LFU caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_keys = [k for k, v in self.frequency.items() if v == min(self.frequency.values())]
                if len(lfu_keys) > 1:
                    lru_lfu_key = None
                    for k in self.usage_order:
                        if k in lfu_keys:
                            lru_lfu_key = k
                            break
                else:
                    lru_lfu_key = lfu_keys[0]
                print("DISCARD:", lru_lfu_key)
                del self.cache_data[lru_lfu_key]
                del self.frequency[lru_lfu_key]
                self.usage_order.remove(lru_lfu_key)
            
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
