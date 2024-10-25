#!/usr/bin/env python3
"""Cache class that creates an instance of a Redis client"""
from collections.abc import Callable
from typing import Optional, Union
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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a randomly generated key

        Args:
        data: The data stored in Redis

        Returns: The randomly generated key used to store the data
        """
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)

        return rand_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[
            Union[str, bytes, int, float]]:
        """
        Retrieve data from Redis and optionally apply a conversion
        function

        Args:
            key (str): The key for the data to be retrieved
            fn (Callable, optional): A function to convert the data
            to the desired type

        Returns:
            Optional[Union[str, int, float, bytes]]: The retrieved and
            possibly converted data, or None
        """
        data = self._redis.get(key)
        if data is None:
            return None

        return fn(data) if fn else data
