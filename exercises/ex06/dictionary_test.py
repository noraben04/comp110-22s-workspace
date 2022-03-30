"""Dictionary py test."""

__author__ = "730437270"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def invert_test() -> None: 
    """Test invert function."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}
    assert invert({'kris': 'jordan', 'michael': 'jordan'}) == KeyError


def fav_color_test() -> None:
    """Test fav color test."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == {"yellow": 1, "blue": 2}
    assert favorite_color({"Marli": "green", "Ella": "purple", "Karie": "green"}) == {"green": 2, "purple": 1}
    assert favorite_color({"Marie": "green", "Mary": "3", "Karie": "green"}) == KeyError


def count_test() -> None:
    """Testing count."""
    assert count(["dog", "dog", "cat", "dog"]) == {"dog": 3, "cat": 1}
    assert count(["dog", "cat", "cat", "dog"]) == {"dog": 2, "cat": 2}
    assert count(["dog", "cat", "3", "dog"]) == KeyError