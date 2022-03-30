"""Tests for the sum function."""


from lessons.sum import sum


def test_sum_empthy() -> None:
    assert sum([]) == 0.0
    