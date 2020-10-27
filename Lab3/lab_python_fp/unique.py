# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.position = 0
        self.unique_elements = set()
        self.elements = items
        if len(kwargs) != 0:
            self.ignore_case = kwargs
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            for element in self.elements:
                current_element = element
                self.position = self.position + 1
                if isinstance(current_element, str):
                    if not (current_element in self.unique_elements) and \
                              not (self.ignore_case and (current_element.lower() in self.unique_elements)):
                        if self.ignore_case:
                            self.unique_elements.add(current_element.lower())
                        else:
                            self.unique_elements.add(current_element)
                        return current_element
                elif (current_element not in self.unique_elements):
                    self.unique_elements.add(current_element)
                    return current_element
            else:
                raise StopIteration

    def __iter__(self):
        return self

# Тест
def main():
    array = ['a', 'a', 'a' , 'A' ,'A', 'b', 'B', 10, 1, 1, 'Boris', 'boris', 'bOrIs', 'Boria']
    iterator1 = Unique(array)
    res1 = []
    iterator2 = Unique(array, ignore_case=True)
    res2 = []
    for i in iterator1:
        res1.append(i)
    print(res1)
    for i in iterator2:
        res2.append(i)
    print(res2)

if __name__ == '__main__':
    main()