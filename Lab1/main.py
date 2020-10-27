import math
import sys


# фамилия
print("Кожуро Б. ИУ5-55Б")

# проверка аргументов КС
a, b, c = 0, 0, 0
correct = False
if len(sys.argv) != 1:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
        correct = True
    except:
        print('неверный ввод из КС')


# ввод аргументов не из КС
if not correct:
    while not correct:
        try:
            a = float(input('Введите a: '))
            correct = True
        except:
            print('неверный ввод, повторите ввод')
            correct = False
    correct = False
    while not correct:
        try:
            b = float(input('Введите b: '))
            correct = True
        except:
            print('неверный ввод, повторите ввод')
            correct = False
    correct = False
    while not correct:
        try:
            c = float(input('Введите c: '))
            correct = True
        except:
            print('неверный ввод, повторите ввод')
            correct = False

# решение уравнения
if a == 0 and b == 0 and c == 0:
    print("Нулевые коэффициэнты. бесконечность решений")
    exit(0)
elif a != 0:
    # проверка на дискриминант
    d = b**2 - 4 * a * c
    if d < 0:
        print('нет решений')
        exit(1)
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        if x1 <0 and x2 < 0:
            print('нет решений')
            exit(2)
        # нахождение корней
        if x1 > 0:
            xa = math.sqrt(x1)
            xb = -math.sqrt(x1)
            print(xa, xb)
        if x2 > 0:
            xc = math.sqrt(x2)
            xd = -math.sqrt(x2)
            print(xc, xd)
        # при нулевом корне x1 или x2 получаем 1 корень 0
        if x1 == 0 or x2 == 0:
            print(0)
# при a==0 и ненулевых других коэффициэнтах
else:
    if (-c/b) > 0:
        x1 = math.sqrt(-c/b)
        x2 = -math.sqrt(-c/b)
        print(x1, x2)
    else:
        print('нет решений')
exit(4)
