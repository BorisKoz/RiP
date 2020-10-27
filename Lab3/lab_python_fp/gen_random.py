import random

def gen_random(count, s, f):
    for i in range(count):
        yield random.randint(s, f)

# тест
def main():
    gen = gen_random(10, 1, 4)
    for i in gen:
        print(i, end=' ')

if __name__ == '__main__':
    main()