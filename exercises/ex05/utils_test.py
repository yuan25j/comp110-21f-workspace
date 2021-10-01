"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730458275"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_even_use_one() -> None:
    """Test one for even."""
    assert only_evens([1, 2, 3, 4]) == [2, 4]
    return None


def test_even_use_edge() -> None:
    """Test two for even."""
    assert only_evens([]) == []
    return None


def test_even_use_two() -> None:
    """Test three for even."""
    assert only_evens([2, 4, 6, 8]) == [2, 4, 6, 8]
    return None


def test_sub_use_one() -> None:
    """Test 1 for sub."""
    assert sub([1, 2, 3], 0, 1) == [1]
    return None


def test_sub_use_edge() -> None:
    """Test 2 for sub."""
    assert sub([], 0, 1) == []
    return None


def test_sub_use_two() -> None:
    """Test 3 for sub."""
    assert sub([0, 2, 4, 5, 6], 0, 4) == [0, 2, 4, 5]
    return None 


def test_concat_use_one() -> None:
    """Test 1 for concat."""
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]
  
    return None


def test_concat_use_two() -> None:
    """Test 2 for concat."""
    assert concat([1], [2]) == [1, 2]
    return None


def test_concat_use_edge() -> None:
    """Test 3 for concat."""
    assert concat([], []) == []
    return None