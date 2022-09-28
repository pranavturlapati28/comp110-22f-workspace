"""This is where we will be testing whether the function skeletons work according to the tests"""

__author__ = "730579095"

from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens() -> None:
    test_list: list[int] = [1,2,3]
    assert only_evens(test_list) == [2]

def test_only_evens_second() -> None:
    test_list: list[int] = [10,21,32,43,54,61]
    assert only_evens(test_list) == [10,32,54]

def test_only_evens_edge() -> None:
    test_list: list[int] = [31, 45]
    assert only_evens(test_list) == []

def test_concat_edge() -> None:
    list_one: list[int] = [1]
    list_two: list[int] = []
    assert concat(list_one, list_two) == [1]

def test_concat() -> None:
    list_one: list[int] = [1]
    list_two: list[int] = [2]
    assert concat(list_one, list_two) == [1,2]

def test_concat_second() -> None:
    list_one: list[int] = [4]
    list_two: list[int] = [2,3,4]
    assert concat(list_one, list_two) == [4,2,3,4]

def test_sub_edge() -> None:
    super_list: list[int] = [1,2,3]
    assert sub(super_list, 0,0) == []

def test_sub() -> None:
    super_list: list[int] = [1,2,3,4,5,6,7]
    assert sub(super_list, 1,4) == [2, 3, 4]

def test_sub_second() -> None:
    super_list: list[int] = [1,2,3,4,5,6,7]
    assert sub(super_list, 0,2) == [1, 2]

