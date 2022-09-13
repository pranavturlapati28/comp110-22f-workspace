"""In this prigram we will be understanding the fundamentals of list functions"""

__author__ = "730579095"

from asyncore import loop


def all(list_parameter: list[int], target_int: int) -> bool:
    """This list returns true if all the values in a list are the same as the target integer"""
    list_length: int = len(list_parameter)
    """The default condition for the function is True, 
    if any on the indices do not equal the target int, it immediately returns False"""
    list_traverse_count: int = 0
    while list_traverse_count < list_length:
        if list_parameter[list_traverse_count] != target_int:
            return False
        list_traverse_count += 1
    return True


def max(list_parameter: list[int]) -> int:
    """Returns the maximum of the given list"""
    if len(list_parameter) == 0:
        raise ValueError("max() arg is an empty List")
    max_value = list_parameter[0]
    loop_traverse: int = 1
    """This function sets the first index to the max, and if any values are greater,
    max is set to that value. The final max is returned"""
    while loop_traverse < len(list_parameter):
        if list_parameter[loop_traverse] > max_value:
            max_value = list_parameter[loop_traverse]
        loop_traverse += 1
    return max_value


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    "If the two lists are deeply equal, we only then return True"
    loop_counter: int = 0
    """The default condition is True, one loop counter compares the two list. If the same index value on both
    lists dont match, it immediately returns false"""
    while loop_counter < len(first_list):
        if first_list[loop_counter] != second_list[loop_counter]:
            return False
        loop_counter += 1
    return True