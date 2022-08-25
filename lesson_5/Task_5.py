"""
Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.
"""
my_list = []
while True:
    line = input("Введите данные: ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + ''
        my_list.append(newline)

    with open("Task_5.txt", "w") as fh:
        fh.writelines(my_list)

"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
"""
my_list = ['Урок номер 5\n', 'Задание 2\n', 'Python\n']
with open("Task_5.txt", 'w+') as file:
    file.writelines(my_list)
with open("Task_5.txt") as file:
    lines = 0
    words = 0
    for line in file:
        lines += 1
        words = len(line.split())
        print(f"{words} Слов в строке")
    print(f"Всего строк {lines}")

"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_4', 'r') as fh:
    content = fh.read().split('\n')
    for i in fh:
        i = i.split('', 1)
        new_file.append(rus[i[0::]])
    print(new_file)

with open('file_4_new', 'w') as fh_2:
    fh_2.writelines(new_file)

"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
FILENAME = "Task5.txt"
DIGITS_STR = "3 19 27 18 1 6 22"
summ = 0
try:
    with open(FILENAME, 'w') as fh:
        fh.write(DIGITS_STR)

    with open(FILENAME, 'r') as fhd:
        data = fhd.read()

    for item in data.split():
        summ += float(item)
except IOError as e:
    print(e)
except ValueError:
    print("Ошибка ввода-вывода")

print(summ)
