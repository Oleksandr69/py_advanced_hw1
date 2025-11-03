# Створіть звичайну функцію множення двох чисел. Створіть карированну
# функцію множення двох чисел. Частково застосуйте її до одного аргументу,
# до двох аргументiв.

def mult(num_1, num_2):
    return num_1 * num_2
print(mult(3, 6))

def carred_mult_1(num_1):
    def carred_mult_2(num_2):
        return num_1 * num_2
    return carred_mult_2
multipl = carred_mult_1(3)
print(multipl(5))