from Lab2.lab_python_oop.FigureColour import FigureColour
from Lab2.lab_python_oop.Rectangle import Rectangle


class Square(Rectangle):

    figure_type = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def __init__(self, a, colour):
        self.a = a
        self.fc = FigureColour()
        self.fc.colourproperty = colour

    def area(self):
        return self.a**2

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            self.fc.colourproperty,
            self.a,
            self.area()
        )
