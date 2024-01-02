#!/usr/bin/python3
"""0. Basic dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A class BasicCache that inherits from BaseCaching

    Attributes:
        MAX_ITEMS: no. of items that can be store in cache
    """

    def put(self, key, item):
        """ Add an item in the cache

        Args:
            key: key of the dict item
            item: value to be added

        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key

         Args:
            key: key of the dict item
        """
        return self.cache_data.get(key, None)
