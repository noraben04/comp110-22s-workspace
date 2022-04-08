"""Dictionary py test."""

__author__ = "730437270"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count
import pytest


def invert_test() -> None: 
    """Test invert function."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def fav_color_test() -> None:
    """Test fav color test."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"
    assert favorite_color({"Marli": "green", "Ella": "purple", "Karie": "green"}) == "green"
    assert favorite_color({"Marie": "green", "Karie": "red"}) == "green"


def count_test() -> None:
    """Testing count."""
    assert count(["dog", "dog", "cat", "dog"]) == {"dog": 3, "cat": 1}
    assert count(["dog", "cat", "cat", "dog"]) == {"dog": 2, "cat": 2}
    assert count([""]) == {"": 0}