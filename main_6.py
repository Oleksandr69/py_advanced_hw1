# Створіть функцію-генератор чисел Фібоначчі. Застосуйте до неї декоратор,
# який залишатиме в послідовності лише парні числа.

def list_decorator(func):
    def wrapper(*arqs, **kwarqs):
        list = []
        result = func(*arqs, **kwarqs)
        for num in result:
            if not num % 2:
                list.append(num)
        return list
    return wrapper

@list_decorator
def fib_list(number):
    list_fib = []
    def fibanacci_num(n):  
        if n < 2:
            return n
        else:
            return fibanacci_num(n-1) + fibanacci_num(n-2)      
    for i in range(number):
        list_fib.append(fibanacci_num(i))
    return list_fib

print(fib_list(25))