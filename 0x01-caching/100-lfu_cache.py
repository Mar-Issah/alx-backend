#!/usr/bin/python3
"""lFU Cache Replacement Implementation Class
"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    An implementation of FIFO(First In Fisrt Out) Cache

    Attributes:
        __keys (list): Stores cache keys
        __rlock (RLock): Lock accessed resources
    """
    def __init__(self):
        """ Instantiation method, sets instance attributes
        """
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """ Add an item in the cache

        Args:
            key: key of the dict item
            item: value to be added
        """
        if key is not None and item is not None:
            key_out = self._cacheUpdate(key)
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
            return self.cache_data.get(key, None)

    def _cacheUpdate(self, key_in):
        """ Method to handle cache size and eviction"""
        key_out = None
        with self.__rlock:
            if key_in not in self.__stats:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = min(self.__stats, key=self.__stats.get)
                    self.cache_data.pop(keyOut)
                    self.__stats.pop(keyOut)
            self.__stats[key_in] = self.__stats.get(key_in, 0) + 1
        return keyOut
