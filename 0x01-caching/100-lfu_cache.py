#!/usr/bin/python3
"""LFU Cache Class"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    An implementaion of LFUCache

    Attributes:
        __cache_keys (list): A dictionary of cache keys
        __rlock (RLock): Lock accessed resources
    """

    def __init__(self):
        """ Instantiation method"""
        super().__init__()
        self.__cache_keys = {}
        self.__rlock = RLock()

    def put(self, key, item):
        """ Add an item in the cache

        Args:
            key: key of the dict item
            item: value to be added
        """
        if key is not None and item is not None:
            key_out = self.__cacheUpdate(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if key_out is not None:
                print('DISCARD: {}'.format(key_out))

    def get(self, key):
        """ Get an item by key

        Args:
            key: key of the dict item
        """
        with self.__rlock:
            value = self.cache_data.get(key, None)
            if key in self.__cache_keys:
                self.__cache_keys[key] += 1
        return value

    def __cacheUpdate(self, key_in):
        """ Method to handle cache size and eviction """
        key_out = None
        with self.__rlock:
            if key_in not in self.__cache_keys:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    key_out = min(self.__cache_keys, key=self.__cache_keys.get)
                    self.cache_data.pop(key_out)
                    self.__cache_keys.pop(key_out)
            self.__cache_keys[key_in] = self.__cache_keys.get(key_in, 0) + 1
        return key_out
