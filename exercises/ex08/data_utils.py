"""Dictionary related utility functions."""

__author__ = "730579095"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], comlumn_name: str) -> list[str]:
    """This function produces a list of strings that is in a column."""
    result: list[str] = []
    for row in table:
        result.append(row[comlumn_name])
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Tranform a row orientation of a table into a column oriented view of a table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], number_rows: int) -> dict[str, list[str]]:
    """Produces a table with the first number of rows."""
    result: dict[str, list[str]] = {}
    if number_rows >= len(table):
        number_rows = len(table)
    for item in table:
        empty_list: list[str] = []
        for i in range(number_rows):
            empty_list.append(table[item][i])
        result[item] = empty_list
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Selects specific content from a table based on values given."""
    result: dict[str, list[str]] = {}
    for item in columns:
        empty_list: list[str] = []
        for i in range(len(table[item])):
            empty_list.append(table[item][i])
        result[item] = empty_list
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Joins two column oriented tables together."""
    result: dict[str, list[str]] = {}
    for item in table1:
        result[item] = table1[item]
    for item in table2:
        if item in result:
            for value in table2[item]:
                result[item].append(value)
        else:
            result[item] = table2[item]
    return result


def count(freq_count: list[str]) -> dict[str, int]:
    """Counts number of times a value is in a list."""
    result: dict[str, int] = {}
    for item in freq_count:
        if item in result: 
            result[item] += 1
        else:
            result[item] = 1
    return result

# Define your functions below
    