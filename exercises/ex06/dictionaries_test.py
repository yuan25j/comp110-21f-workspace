"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730458275"

from exercises.ex06.dictionaries import invert
from exercises.ex06.dictionaries import count
from exercises.ex06.dictionaries import favorite_color


def test_invert_1() -> None:
    """Test for invert."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}
    return None


def test_invert_2() -> None:
    """Test for invert 2."""
    test_dict: dict[str, str] = {"Example": "Not Example"}
    assert invert(test_dict) == {"Not Example": "Example"}
    return None


def test_invert3() -> None:
    """Test for invert 3."""
    test_dict: dict[str, str] = {"One": "Two", "Three": "Four"}
    assert invert(test_dict) == {"Two": "One", "Four": "Three"}
    return None
                                                                     

def test_count1() -> None:
    """Test for count."""
    test_list = []
    assert count(test_list) == {}
    return None


def test_count2() -> None:
    """Test for count 2."""
    test_list: list[str] = ["1"]
    assert count(test_list) == {"1": 1}
    return None


def test_count3() -> None:
    """Test for count 3."""
    test_list: list[str] = ["1", "1"]
    assert count(test_list) == {"1": 2}
    return None


def test_favorite1() -> None:
    """Test for favorite 1."""
    test_dict: dict[str, str] = {"Max": "Yellow"}
    assert favorite_color(test_dict) == "Yellow"
    return None

    
def test_favorite2() -> None:
    """Test for favorite 1."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""
    return None


def test_favorite3() -> None:
    """Test for favorite 2."""
    test_dict: dict[str, str] = {"Max": "Yellow", "Alice": "Green"}
    assert favorite_color(test_dict) == "Yellow"
    return None