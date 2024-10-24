#!/bin/env python3
"""Cache class"""
import uuid
import redis


class Cache():
    """
    Initialize the Cache class with a Redis client and flush the
    database keys
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data) -> str:
        """
        Store the input data in Redis with a randomly generated key

        Args:
        data: The data stored in Redis

        Returns: The randomly generated key used to store the data
        """
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)

        return rand_key
