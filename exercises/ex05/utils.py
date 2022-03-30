"""list utility functions."""

__author__ = "730437270"


def only_evens(num_list: list[int]) -> list[int]:
    """Return only even."""
    alist = []
    for i in num_list:
        if i % 2 == 0:
            alist.append(i)
    return alist


def sub(give_list: list[int], start_in: int, end_in: int) -> list[int]:
    """Generate a subset of a given list."""
    sublist = []
    i: int = start_in
    if start_in < 0:
        start_in = 0
    if end_in > len(give_list):
        end_in = len(give_list)
    while i < end_in: 
        sublist.append(give_list[i])
        i = i + 1
    return sublist


def concat(first_list: list[int], sec_list: list[int]) -> list[int]:
    """Will produce new list that contains both lists."""
    newnew_list = []
    for i in first_list:
        newnew_list.append(i)
    for i in sec_list:
        newnew_list.append(i)
    return newnew_list