"""Unit test."""

__author__ = "730437270"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens() -> None:
    """Test only even functions."""
    assert only_evens([1, 2, 3]) == [2]
    assert only_evens([1, 5, 3]) == []
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_sub() -> None: 
    """Test sub functions."""
    assert sub([10, 20, 30, 40, 1, 3], 1, 3) == [20, 30]
    assert sub([20, 30, 40, 1, 3], 1, 3) == [30, 40]
    assert sub([30, 40, 2, 3], 2, 3) == [2]


def test_concat() -> None: 
    """Test concat functions."""
    assert concat([1, 2, 3, 4], [5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert concat([8, 9, 10], [12, 13]) == [8, 9, 10, 12, 13]
    assert concat([2, 4, 6], [1, 3]) == [2, 4, 6, 1, 3]