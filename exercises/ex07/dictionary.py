"""Creating dictionary functions and using pytest to see if their implementation is correct."""

__author__ = "730579095"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """Switches keys to being values and values to keys. If duplicate keys exist, raises KeyError."""
    new_dict: dict[str, str] = {}
    values: list[str] = []
    for index in xs:
        if xs[index] not in values:
            new_dict[xs[index]] = index
            values.append(xs[index])
        else:
            raise KeyError
    return new_dict


def favorite_color(fd: dict[str, str]) -> str:
    """With a provided list of students favorite colors, it returns the color that is the most commonly said."""
    colors_counts: dict[str, int] = {}
    colors: list[str] = []
    for key in fd:
        if fd[key] not in colors:
            colors_counts[fd[key]] = 1
            colors.append(fd[key])
        else:
            colors_counts[fd[key]] += 1
    for key in colors_counts:
        if colors_counts[key] == max(colors_counts.values()):
            return key
    

def count(xs: list[str]) -> dict[str, int]:
    """Creates a dict with each unique value and finds the amount of times it occurs in a list."""
    result_dict: dict[str, int] = {}
    for index in xs:
        if index in result_dict:
            result_dict[index] += 1
        else:
            result_dict[index] = 1
    return result_dict