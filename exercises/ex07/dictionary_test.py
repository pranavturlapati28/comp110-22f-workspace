"""This is to create tests for the functions that use dictionaries."""

__author__ = "730574526"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_1() -> None:
    """Makes sure the function works when given an empy dictionary as a parameter."""
    assert invert({}) == {}


def test_invert_2() -> None:
    """This is a use case check."""
    assert invert({"five": "FIVE", "four": "FOUR"}) == {"FIVE": "five", "FOUR": "four"}


def test_invert_3() -> None:
    """This is another use case check."""
    assert invert({"key": "value"}) == {"value": "key"}


def test_favorite_color_1() -> None:
    """This checks what happens if two colors have the same frequency."""
    assert favorite_color({"Jack": "Purple", "Nandan": "White"}) == "Purple"


def test_favorite_color_2() -> None:
    """This is a use case check."""
    assert favorite_color({"amy": "purple", "alice": "purple", "andy": "white"}) == "purple"


def test_favorite_color_3() -> None:
    """This is another use case check."""
    assert favorite_color({"arnold": "purple"}) == "purple"


def test_count_1() -> None:
    """This checks if the function works when given a dictionary with only one key."""
    assert count(["one"]) == {"one": 1}


def test_count_2() -> None:
    """This is a use case check."""
    assert count(["water", "water", "milk"]) == {"water": 2, "milk": 1}


def test_count_3() -> None:
    """This is another use case check."""
    assert count(["milk", "pine", "cedar"]) == {"milk": 1, "pine": 1, "cedar": 1}