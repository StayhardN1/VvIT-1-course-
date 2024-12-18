a = input('Выберите вариант чтения 1 или 2: ')
print(a)
if int(a)==1:
    f = open(r"/Users/kurbangasanov/PycharmProjects/n1/Лаба 3/example.txt").read()
    print(f)
else:
    f = open(r"/Users/kurbangasanov/PycharmProjects/n1/Лаба 3/example.txt").readlines()
    print(f)


a=input('Введите текст файла:')
b=input('Дополните текст файла:')
new_file = open("/Users/kurbangasanov/PycharmProjects/n1/Лаба 3/.venv/user_input.txt," "w+")
new_file.write(a)
new_file = open("user_input.txt", "a+")
new_file.write('\n' + b)
new_file.close()

a = input('Выберите вариант чтения 1 или 2' )
print(a)
try:
    if int(a)==1:
        f=open(r"/Users/kurbangasanov/PycharmProjects/n1/Лаба 3/example.txt").read()
        print(f)
    else:
        f=open(r"/Users/kurbangasanov/PycharmProjects/n1/Лаба 3/example.txt").readlines()
        print(f)
except FileNotFoundError:
    print("Файл не найден")