import numpy
from Lab2.lab_python_oop.Circle import Circle
from Lab2.lab_python_oop.Rectangle import Rectangle
from Lab2.lab_python_oop.Square import Square

# фамилия
print("Кожуро Б. ИУ5-55Б")

# проверка фигур

def main():
    r = Rectangle(8, 8, 'синего')
    c = Circle(8, 'зеленого')
    s = Square(8, 'красного')
    print(r)
    print(c)
    print(s)
    a = numpy.array([1, 2, 3])
    print(type(a))

if __name__ == "__main__":
    main()

