from behave import *
from adapter import circle
from adapter import roundhole
from adapter import area
from adapter import adapter


@given('circle r={circle_r}, hole r={hole_r}')
def step(context, circle_r, hole_r):
    context.circle = circle(int(circle_r))
    context.hole = roundhole(int(hole_r))


@given('area x={x}, y={y}, hole r={hole_r}')
def step(context, x, y, hole_r):
    context.area = area(int(x), int(y))
    context.hole = roundhole(int(hole_r))


@then('Проходит')
def step(context):
    assert context.hole.fits(context.circle) == f"влезает , радиус детали= {context.circle.get_r()} " \
                                                      f"и отверстия={context.hole.get_r()}"


@then('Не Проходит')
def step(context):
    assert context.hole.fits(context.circle) == f"не влезает , радиус детали= {context.circle.get_r()} " \
                                                      f"и отверстия={context.hole.get_r()}"


@then('С адаптером прямоугольник проходит')
def step(context):
    context.adapted = adapter(context.area)
    assert context.hole.fits(context.area) == f"влезает , радиус детали= {context.adapted.get_r()} " \
                                                 f"и отверстия={context.hole.get_r()}"


@then('С квадратом прямоугольник не проходит')
def step(context):
    context.adapted = adapter(context.area)
    assert context.hole.fits(context.adapter) == f"не влезает , радиус детали= {context.adapted.get_r()} " \
                                                 f"и отверстия={context.hole.get_r()}"
