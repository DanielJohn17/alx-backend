#!/usr/bin/env python3
'''Module with FIFO cache system'''
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO cache system that inherits from BaseCaching'''

    def __init__(self):
        '''Init method'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds an item to the cache'''
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        '''Gets an item by key'''
        return self.cache_data.get(key, None)
