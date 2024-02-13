from typing import Literal

from robot.api.deco import keyword


@keyword('Number of ${animals} should be')
def number_of_animals_should_be(animals, count: 'int | float'):
    print(animals, count)


def turn(direction: Literal['left', 'right']) -> str:
    print(direction)
