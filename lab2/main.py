def greet(name):
    print(f"Привет, {name}!")
greet("Курбан")


def square(number):
    return number ** 2
result = square(16)
print(f"Квадрат числа 16 равен {result}")



def max_of_two(num1, num2):
    return num1 if num1 > num2 else num2
max_number = max_of_two(14,88)
print(f"Большее из чисел 14 и 88: {max_number}")