"""List utility functions."""

__author__ = "730458275"


def all(list_one: list[int], number: int) -> bool:
    """Checks if number is in the list."""
    i = 0
    
    if len(list_one) == 0:
        return False
    while i < len(list_one):
        if number != list_one[i]:
            return False
        i += 1
    return True


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Checks if two lists are equal."""
    if len(list_one) != len(list_two):
        return False
    i = 0
    while i < len(list_one):
        if list_one[i] != list_two[i]:
            return False
        i += 1
    return True


def max(list_one: list[int]) -> int:
    """Returns the largest value in the list."""
    i = 0
    largest_number = list_one[0]
    while i < len(list_one):
        if largest_number < list_one[i]:
            largest_number = list_one[i]
        i += 1
    return largest_number
