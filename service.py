from pydantic import BaseModel
import random


class Equation(BaseModel):
    a: int
    b: int
    c: int


def equation(item: Equation):
    discr = (item.b ** 2) - (4 * item.a * item.c)
    print(discr)
    if discr < 0:
        return False
    if discr == 0:
        x = -item.b / (2 * item.a)
        return {'x': x}
    if discr > 0:
        x1 = (-item.b + discr ** .5) / (2 * item.a)
        x2 = (-item.b - discr ** .5) / (2 * item.a)
        return {'x1': x1, 'x2': x2}


def color_hint(item: int):
    b = 70
    g = 20
    r = 10
    res = random.randint(1, 100)
    res -= b
    if res < 0:
        return {item: 'blue'}
    res -= g
    if res < 0:
        return {item: 'green'}
    res -= r
    if res < 0:
        return {item: 'red'}

