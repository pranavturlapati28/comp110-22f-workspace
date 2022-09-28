"""This is where we will be writing function implementations"""

__author__ = "730579095"

def only_evens(xs: list[int]) -> list[int]:
    """This function returns a new list with only the even items"""
    new_list: list[int] = list()
    for item in xs:
        if item % 2 == 0:
            new_list.append(item)
    return new_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """This list combines two lists"""
    new_list: list[int] = first_list
    for item in second_list:
        new_list.append(item)
    return new_list
    
def sub(super_list: list[int], first_index: int, second_index: int) -> list[int]:
    """This list creates a subset of the super_list that starts at the first index and ends at the second index"""
    subset_list: list[int] = list()
    index_counter: int = first_index
    while index_counter < second_index:
        subset_list.append(super_list[index_counter])
        index_counter += 1
    return subset_list


    