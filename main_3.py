# Напишіть програму яка буде виводити 25 перших чисел Фібоначі, використовуючи для цього три наведені в
# тексті заняття функції — без кешу, з кешем довільної довжини, з кешем з модулю functools з
# максимальною кількістю 10 елементів та з кешем з модулю functools з максимальною кількістю 16 елементів.

def fibonacci_num(number, add_num):
    if number < 0:
        numbers_list = []
        return numbers_list
    elif number == 1:
        numbers_list = [0]
        return numbers_list
    else:
        numbers_list = [0, 1]
        while len(numbers_list) < number:
            # next_number = numbers_list[-1] + numbers_list[-2]
            numbers_list.append(add_num(numbers_list[-1], numbers_list[-2]))
        return numbers_list
    
add = lambda x, y: x + y
print(fibonacci_num(21, add))


# ==================================================================

 