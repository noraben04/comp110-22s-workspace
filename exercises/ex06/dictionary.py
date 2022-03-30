"""Dictionary, function skeleton."""

__author__ = "730437270"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Invert dictionary keys and values."""
    empty = {}
    for key in d:
        value = d[key]
        if value in empty:
            raise KeyError("WRONG")
        else:
            empty[value] = key 
    return empty
    

def favorite_color(i: dict[str, str]) -> str:
    """Assessing most common color."""
    empty = {}
    for key in i:
        value = i[key]
        if value in empty:
            empty[value] = empty[value] + 1
        else:
            empty[value] = 1
    pop_color = 0
    color_pop = ""
    for value in empty:
        color_num = empty[value]
        if color_num > pop_color:
            pop_color = color_num
            color_pop = value 
    return color_pop


def count(c: list[str]) -> dict[str, int]:
    """Count of each item in the list."""
    empty = {}
    for i in c:
        if c in empty:
            empty[c] += 1
        else:
            empty[c] = 1
    return empty