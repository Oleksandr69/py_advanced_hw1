from colorama import Fore
from functools import partial
from functools import lru_cache
import time
def color_decorator(color):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(color, end = "")
            result = func(*args, **kwargs)
            print(Fore.RESET, end="")
            return result
        return wrapper
    return decorator

# @color_decorator(Fore.GREEN)
# def print_hello():
#     print("Hello world!")
# print_hello()

# @color_decorator(Fore.BLUE)
# def print_hello():
#     print("Hello world!")
# print_hello()

@color_decorator(Fore.GREEN)
def power(num_1, num_2):
    print(f"{num_1} in power {num_2} is {num_1 ** num_2}")

square_power = partial(power, num_2=2)
square_power(10)

@lru_cache
def number(num):
    time.sleep(2)
    return num
print(number(11))
print(number(11))

cache_data = {}
def my_cache(func):
    def wrapper(*args, **kwargs):
        key = f"{func.__name__}-{args}-{kwargs}"
        if key in cache_data:
            return cache_data[key]
        else:
            result = func(*args, **kwargs)
            cache_data[key] = result
            return result
    return wrapper