from Lab2.lab_python_oop.FigureAbstract import FigureAbstract
from Lab2.lab_python_oop.FigureColour import FigureColour
import math


class Circle(FigureAbstract):

    figure_type = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def __init__(self, radius, colour):
        self.radius = radius
        self.fc = FigureColour()
        self.fc.colourproperty = colour

    def area(self):
        return math.pi*(self.radius**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.fc.colourproperty,
            self.radius,
            self.area()
        )
