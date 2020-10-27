def print_result(f):
    def decorated(*args):
        print(f.__name__)
        res = f(*args)
        #сверка типа
        if isinstance(res, list):
            for i in res:
                print(i)
        elif isinstance(res, dict):
            for i in res:
                print(i, ' = ', res.get(i))
        else:
            print(res)
        return res
    return decorated

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()