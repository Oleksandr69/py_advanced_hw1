# Напишіть програму яка буде виводити 25 перших чисел Фібоначі, використовуючи для цього три наведені в
# тексті заняття функції — без кешу, з кешем довільної довжини, з кешем з модулю functools з
# максимальною кількістю 10 елементів та з кешем з модулю functools з максимальною кількістю 16 елементів.
from functools import lru_cache
list_fib = []
def fibanacci_num(n):  
    if n < 2:
        return n
    else:
        return fibanacci_num(n-1) + fibanacci_num(n-2)
    
for i in range(25):
    list_fib.append(fibanacci_num(i))
print(list_fib)
# ==================================================================
@lru_cache(maxsize=None)
def fibanacci(num):
    if num < 2:
        return num
    else:
        return fibanacci(num-1) + fibanacci(num-2)
    
list = [fibanacci(i) for i in range(25)]
print(list)
# ==================================================================
@lru_cache(maxsize=10)
def fiban(num):
    if num < 2:
        return num
    else:
        return fibanacci(num-1) + fibanacci(fibanacci_num-2)
    
list_10 = [fibanacci(i) for i in range(25)]
print(list_10)
# ==================================================================
@lru_cache(maxsize=16)
def fib(num):
    if num < 2:
        return num
    else:
        return fibanacci(num-1) + fibanacci(fibanacci_num-2)
    
list_16 = [fibanacci(i) for i in range(25)]
print(list_16)
# ================================================================== 
# cache_data = {}
# def my_cache(func):
#     def wrapper(*args, **kwargs):
#         key = f"{func.__name__}-{args}-{kwargs}"
#         if key in cache_data:
#             return cache_data[key]
#         else:
#             result = func(*args, **kwargs)
#             cache_data[key] = result
#             return result
#     return wrapper
# ==================================================================

 