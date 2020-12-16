# структурный паттерн проектирования
# адаптер
# предметная область: проверка, входит ли кпрямоугольная деталь в круглое отверстие.


# класс круглых деталей
from math import sqrt


class circle:
    def __init__(self, r):
        self.r = r
    def get_r(self):
        return self.r


# класс прямокгольниак
class area:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y


# класс  отверстия
class roundhole:

    def __init__(self, r):
        self.r = r

    def get_r(self):
        return self.r

    def fits(self, detail):

        if self.get_r() >= detail.get_r():
            return f"влезает , радиус детали= {detail.get_r()} и отверстия={self.get_r()}"
        else:
            return f"не влезает , радиус детали= {detail.get_r()} и отверстия={self.get_r()}"


# адаптер
class adapter(area):

    def __init__(self, area):
        self.area = area

    def get_r(self):
        return sqrt((self.area.get_x() / 2)**2 + (self.area.get_y() / 2)**2)


def client_code():
    circle1 = circle(10)
    circle2 = circle(20)
    area1 = area(8, 9)
    area2 = area(20, 16)
    hole = roundhole(12)
    print(hole.fits(circle1))
    print(hole.fits(circle2))
    print(hole.fits(adapter(area1)))
    print(hole.fits(adapter(area2)))


if __name__ == "__main__":

    client_code()
