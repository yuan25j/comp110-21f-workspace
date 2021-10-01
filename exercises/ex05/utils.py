"""List utility functions part 2."""

__author__ = "730458275"


# Define your functions below
def only_evens(xs: list[int],) -> list[int]:
    """Returns list of even numbers."""
    new_list: list[int] = []
    for number in xs:
        if number % 2 == 0:
            new_list.append(number)
        
    return new_list


def sub(xs: list[int], int_one: int, int_two: int) -> list[int]:
    """Creates a new list."""
    new_list: list[int] = []
    i = 0
    while i < len(xs):
        x = xs[i]
        if i >= int_one and i <= (int_two - 1):
            new_list.append(x)
        i += 1
    return new_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Concats two different lists into one."""
    new_list: list[int] = []
    for x in xs:
        new_list.append(x)
    for y in ys:
        new_list.append(y)
    return new_list
