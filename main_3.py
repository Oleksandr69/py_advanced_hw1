add = lambda x, y: x + y
def fibonacci_num(number):
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
            numbers_list.append(add(numbers_list[-1], numbers_list[-2]))
        return numbers_list

print(fibonacci_num(25))