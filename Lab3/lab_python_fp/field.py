def field(items, *args):
    values = []
    try:
        assert len(args) > 0
    except:
        print('нет аргументов')
        return []
    if len(args) == 1:
        for item in items:
            val = item.get(args[0])
            if val is not None:
                values.append(val)
    else:
        for item in items:
            dic = {}
            for arg in args:
                val = item.get(arg)
                if val is not None:
                    dic[arg] = val
            if len(dic) != 0:
                values.append(dic)
    return values

# тест
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стол', 'price': None, 'color': 'white'},
]

def main():
    print('Пример 1:')
    print(field(goods, 'title'))
    print('\n', 'Пример 2:')
    print(field(goods, 'title', 'color'))

if __name__ == '__main__':
    main()
