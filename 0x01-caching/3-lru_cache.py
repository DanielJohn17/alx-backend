#!/usr/bin/env python3
'''Module with LRU cache system'''
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''LRU cache system that inherits from BaseCaching'''

    def __init__(self):
        '''Init method'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds an item to the cache'''
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD: {}".format(lru_key))

            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''Gets an item by key'''
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
