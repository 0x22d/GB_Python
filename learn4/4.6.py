#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from typing import Iterable
from itertools import cycle


def get_repeated(iterable: Iterable, count: int):
    """
    Создает генератор на count раз с iterable
    :param iterable: итерируемый повторяемый объект
    :param count: сколько раз повторить
    """

    if not isinstance(count, int):
        raise TypeError(f"count '{count.__class__.__name__}' is illegat type")

    if count < 0:
        raise ValueError(f"count 'can't be less than 0")


    iterator = cycle([iterable])

    while count:
        yield next(iterator)
        count -= 1


if __name__ == '__main__':
    source_list = [1, 2, 3]
    repeat = 4

    print(list(get_repeated(source_list, repeat)))