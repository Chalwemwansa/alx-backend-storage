#!/usr/bin/env python3
"""this script contains a python class Cache that
stores an instance of redis"""
import redis
import uuid
import functools
from typing import Union, Optional, Callable


def replay(store: str) -> None:
    """the function replays all the commands issued and their output"""
    #  create a redit instance
    r = redis.Redis(decode_responses=True)
    #  get the inputs list and the outputs list from redit
    method_name = store.__qualname__
    input_key = method_name + ":inputs"
    output_key = method_name + ":outputs"

    #  get the lists from the redit db
    input_list = r.lrange(input_key, 0, -1)
    output_list = r.lrange(output_key, 0, -1)

    #  zip the output so that you make tuples
    in_out = zip(input_list, output_list)

    for command_return in list(in_out):
        command, returned = command_return
        print(f'{method_name}(*{command}) -> {returned}')


def count_calls(method: Callable) -> Callable:
    """the function that is used to automatically increment
    num of times a given function is called as a decorator function"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """the wrapper function that does the necessary things then returns
        the actual call later on"""
        key = method.__qualname__  # get the qualified name of the method
        self._redis.incr(key)  # Increment count for the method
        return method(self, *args, **kwargs)  # Call original method
    return wrapper


def call_history(method: Callable) -> Callable:
    """a wrapper class that gets the input and the output from
    a called method"""
    @functools.wraps(method)
    def Wrap(self, *args, **kwargs):
        """wrapper function that does the storage of two lists for input
        and output of a function"""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))
        #  execute the called method and get the output
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return Wrap


class Cache:
    """class that initialises a redis database"""
    def __init__(self):
        """initialises the _redis private instance that maps
        to the redis api"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """the stores method that returns a random generated key and returns
        it as a string"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """the class that gets the actual datatype of the value
        of a given key"""
        if fn is not None:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """automativally parametarizes the get function"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """returns the int representation of the value from the redis db"""
        return self.get(key, int)
