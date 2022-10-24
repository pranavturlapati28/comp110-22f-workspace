"""Creating functions that use dictionaries."""

__author__ = "730574526"
 
 
def invert(dict1: dict[str, str]) -> dict[str, str]:
    """This function swaps the keys and values."""
    dict2: dict[str, str] = {}
    for key in dict1:
        dict2[dict1[key]] = key
    return dict2
 
 
def favorite_color(dict1: dict[str, str]) -> str:
    """This function returns the color that appears the most."""
    return max(set(list(dict1.values())), key = list(dict1.values()).count)


def count(list: list[str]) -> dict[str, int]:
    """This function returns a dictionary with each value and its frequency."""
    dict: dict[str, int] = {}
    for thing in list:
        if thing in dict:
            dict[thing] += 1
        else:
            dict[thing] = 1
    return dict