#!/usr/bin/env python3

import redis

Cache = __import__('exercise').Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

print("before going into db the values were:")
for value in TEST_CASES.keys():
    print(value)

print("after going into db the values were:")
for value, fn in TEST_CASES.items():
    key = cache.store(value)
    print(cache.get(key, fn=fn))
    if not fn is None:
      print("using the get_str and get_int:")
    if fn == int:
      print(cache.get_int(key))
    elif not fn is None:
      print(cache.get_str(key))
    print()
