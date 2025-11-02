# Створіть список цілих чисел. Отримайте список квадратів непарних чисел із
# цього списку.
def list_decorator(func):
    def wrapper(*arqs, **kwarqs):
        list = []
        result = func(*arqs, **kwarqs)
        for num in result:
            if num % 2:
                list.append(num ** 2)
        return list
    return wrapper

@list_decorator
def numbers(start, stop, step):
    numbers_list = []
    for i in range(start, stop, step):
        numbers_list.append(i)
    return numbers_list

print(numbers(-10, 15, 1))