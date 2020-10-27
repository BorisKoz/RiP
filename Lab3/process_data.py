from Lab3.lab_python_fp.cm_timer import cm_timer_1
from Lab3.lab_python_fp.print_result import print_result
from Lab3.lab_python_fp.unique import Unique
from Lab3.lab_python_fp.field import field
from Lab3.lab_python_fp.gen_random import gen_random
import json
import sys
import os


path = os.getcwd()+'\\data_light.json'
with open(path, encoding='utf-8') as f:
    data = json.load(f)



# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return Unique(field(arg, 'job-name'), ignore_case=True)


@print_result
def f2(arg):
    return filter(lambda x:  x.startswith('Программист'), arg)


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    salary = gen_random(len(arg), 100000, 200000)
    return list(zip(arg, salary))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
