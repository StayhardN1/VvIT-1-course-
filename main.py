num = int(input("Введите число: "))
for i in range(1, num + 1):
    print(i)


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if num1 > num2:
    print("Большее число:", num1)
elif num2 > num1:
    print("Большее число:", num2)
else:
    print("Оба числа равны")