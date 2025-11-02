# За допомогою написаного Вами декоратору заміряйте та порівняйте швидкість роботи цих
# 4х варіантів.

from functools import lru_cache
import time

def time_meter_decorator(func):
    def wrapper(*arqs, **kwarqs):
        start_time = time.time()
        result = func(*arqs, **kwarqs)
        print(time.time() - start_time)
        return result
    return wrapper

list_fib = []

@time_meter_decorator
def fib_list(number):
    def fibanacci_num(n):  
        if n < 2:
            return n
        else:
            return fibanacci_num(n-1) + fibanacci_num(n-2)      
    for i in range(number):
        list_fib.append(fibanacci_num(i))
    return list_fib

print(fib_list(25))

# lru_cache(maxsize=None)
print("lru_cache()")
@time_meter_decorator
@lru_cache
def fibanacci_list(number):
    def fibanacci(num):
        if num < 2:
            return num
        else:
            return fibanacci(num-1) + fibanacci(num-2)   
    list = [fibanacci(i) for i in range(number)]
    return list
print(fibanacci_list(25))

# lru_cache(maxsize=10)
print("lru_cache(maxsize=10)")
@time_meter_decorator
@lru_cache(maxsize=10)
def fibanacci_list_10(number):
    def fibanacci(num):
        if num < 2:
            return num
        else:
            return fibanacci(num-1) + fibanacci(num-2)   
    list = [fibanacci(i) for i in range(number)]
    return list

print(fibanacci_list_10(25))

# lru_cache(maxsize=16)
print("lru_cache(maxsize=16)")
@time_meter_decorator
@lru_cache(maxsize=16)
def fibanacci_list_16(number):
    def fibanacci(num):
        if num < 2:
            return num
        else:
            return fibanacci(num-1) + fibanacci(num-2)   
    list = [fibanacci(i) for i in range(number)]
    return list

print(fibanacci_list_16(25))

# ================================================================== 