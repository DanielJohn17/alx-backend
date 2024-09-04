#!/usr/bin/env python3
'''Module with MRU cache system'''
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''MRU cache system that inherits from BaseCaching'''

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
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD: {}".format(mru_key))

            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        '''Gets an item by key'''
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
