from Lab2.lab_python_oop.FigureAbstract import FigureAbstract
from Lab2.lab_python_oop.FigureColour import FigureColour


class Rectangle(FigureAbstract):

    figure_type = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def __init__(self, a, b, colour):
        self.a = a
        self.b = b
        self.fc = FigureColour()
        self.fc.colourproperty = colour

    def area(self):
        return self.a * self.b

    def __repr__(self):
        return '{} {} цвета со сторонами {} на {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.fc.colourproperty,
            self.a,
            self.b,
            self.area()
        )
