import math
from functools import wraps
def result_cache_decorator(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = (args, frozenset(kwargs.items()))
        if cache_key in cache:
            return cache[cache_key]
        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result
    return wrapper
@result_cache_decorator
def custom_sqrt(x):
    return math.sqrt(x)

print(custom_sqrt(4))
print(custom_sqrt(4))
print(custom_sqrt(x=4))
print(custom_sqrt(x=4))