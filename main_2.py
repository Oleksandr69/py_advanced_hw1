# Напишіть декоратор, який буде заміряти час виконання для наданої функції.
import time
def time_meter_decorator(func):
    def wrapper(*arqs, **kwarqs):
        start_time = time.time()
        result = func(*arqs, **kwarqs)
        print(time.time() - start_time)
        return result
    return wrapper

@time_meter_decorator
def print_hello():
    print("hello")

print(print_hello())

@time_meter_decorator
def sum(num_1: int, num_2: int):
    return num_1 + num_2

print(sum(3, 5))