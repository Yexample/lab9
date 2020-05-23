import os

def manualInput(question):
    answer = input(question + "(y/n): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Введите y или n")
        answer = input(question + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False

# Перевести в 10 систему
def decimalConversion(number, base):
    try:
        decimalNumber = int(number, base)

    except Exception:
        print("Ошибка в файле входных данных. Первый элемент в строке должен быть целым числом в системе счисления с базой от 2 до 16")
        exit(1)
    else:
        return decimalNumber

# Перевести цифры в буквы для систем с количеством цифр > 10
def digitConversion(digit):
    if digit < 10:
        return str(digit)
    else:
        return chr(ord('A') + digit - 10)

# Перевести число из 10 системы в желаемую
def nthBaseConversion(number, base):
    if number < 0:
        return '-' + nthBaseConversion(-number, base)
    else:
        (result, remainder) = divmod(number, base)
        if result > 0:
            return nthBaseConversion(result, base) + digitConversion(remainder)
        return digitConversion(remainder)


# main

while True:
    try:
        name1 = input("Введите имя файла с исходными данными ")
        f = open(name1)
        if os.stat(name1).st_size == 0:
            raise Exception
    except FileNotFoundError:
        print("Ошибка. Файл не существует")
    except Exception:
        print("Ошибка. Файл пуст")
    else:
        f.close()
        break

name2 = input("Введите имя файла с для записи результатов ")


if manualInput("Обновить файл с исходными данными?"):
    H1 = input("1 число ")
    P1 = input("База системы счисления 1 числа ")
    H2 = input("2 число ")
    P2 = input("База системы счисления 2 числа ")

    numbers = open(name1, "w")
    print(H1, P1, file=numbers)
    print(H2, " ", P2, file=numbers)
    numbers.close()
else:
    pass

number, base = [], []

numbers = open(name1)

for line in numbers:
    row = line.split()
    number.append(row[0])
    try:
        base.append(int(row[1]))
    except Exception:
        print("Ошибка в файле входных данных. Второе число строки после пробела должно быть целым.")
        exit(1)
numbers.close()

try:
    x = decimalConversion(number[0], base[0])
    y = decimalConversion(number[1], base[1])

except Exception:
    print("Ошибка в файле входных данных. Файл должен содержать 2 строки")
    exit(1)
else:
    sum10 = x + y
    print("x = ", x, "; y =", y, "; sum10 = ", sum10, "\n")

sumA = nthBaseConversion(sum10, base[0])
sumB = nthBaseConversion(sum10, base[1])

# print("Сумма в ", base[0], "системе счисления = ", sumA)
# print("Сумма в ", base[1], "системе счисления = ", sumB)

output = open(name2, "w")

for i in base:
    sumi = nthBaseConversion(sum10, base[base.index(i)])
    print("Сумма в ", i, "системе счисления = ", sumi)
    print("Сумма в ", i, "системе счисления = ", sumi, file = output)

output.close()
