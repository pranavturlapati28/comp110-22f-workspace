"""Creating unit tests for the functions we had previously created in dictionary.py."""

__author__ = "730579095"


import pytest
from exercises.ex07.dictionary import invert, favorite_color, count


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_invert_use_case() -> None:
    """Tests a normal random use case."""
    current_dict: dict[str, str] = {"John": "James", "Apple": "Orange", "Pie": "Peach"}
    assert invert(current_dict) == {"James": "John", "Orange": "Apple", "Peach": "Pie"}


def test_invert_use_case2() -> None:
    """This testa a another random normal test use case."""
    current_dict: dict[str, str] = {"I": "me", "loves": "adores", "CS": "computer"}
    assert invert(current_dict) == {"me": "I", "adores": "loves", "computer": "CS"}


def test_invert_edge_case() -> None:
    """Tests what happens whether an error occurs if an empty list is provided."""
    current_dict: dict[str, str] = {}
    assert invert(current_dict) == {}


def test_favorite_color_normal_case() -> None:
    """Tests a nroaml use case for the favorite color function."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_normal_case2() -> None:
    """Tests a nroaml use case for the favorite color function."""
    test_dict: dict[str, str] = {"Pranav": "blue", "Kris": "blue", "James": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_edge_case() -> None:
    """Tests if tie for mode exists, will it provide the first one in the dictionary."""
    test_dict: dict[str, str] = {"Pranav": "purple", "Kris": "blue", "Roshan": "red"}
    assert favorite_color(test_dict) == "purple"


def test_count_normal_case() -> None:
    """Tests a normal use case for the count function."""
    assert count(["piza", "pizza", "piza", "piza", "Pranav"]) == {'piza': 3, 'pizza': 1, 'Pranav': 1}


def test_count_normal_case2() -> None:
    """Tests a normal use case for the count function with no unique values."""
    assert count(["piza1", "pizza", "piza2", "piza3", "Pranav"]) == {'piza1': 1, 'pizza': 1, 'piza2': 1, 'piza3': 1, 'Pranav': 1}


def test_count_edge_case() -> None:
    """Tests an edge case when there is only one value in the list."""
    assert count(["Pranav"]) == {"Pranav": 1}