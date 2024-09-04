#!/usr/bin/env python3
'''Module with BasicCache class'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''''Inherits from BaseCaching and is a caching system'''

    def put(self, key, item):
        '''Puts an item in cache'''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''Gets an item by key'''
        return self.cache_data.get(key, None)
