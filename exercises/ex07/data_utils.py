"""Dictionary related utility functions."""

__author__ = "730437270"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]: 
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")
     
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Produce list of stings of all values in a single column from second parameter."""
    final_column = []
    for dictionary_row in table:
        final_column.append(dictionary_row[column_name])
    return final_column


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform table represented as list of rows into dict of columns."""
    final_dict = {}
    column_name = []
    for dictionary_row in table:
        for column_name in dictionary_row:
            final_dict[column_name] = column_values(table, column_name)

    return final_dict
    
        
def head(dict_table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Create new column-based table with only N rows of data for each column."""
    final_dict = {}
    for key in dict_table:
        n_values = []
        count = 0
        for i in dict_table[key]:
            if count < num_rows:
                n_values.append(i)
                count += 1
        final_dict[key] = n_values

    return final_dict


def select(dict_table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only specific subset of og columns."""
    final_dict = {}
    for col_name in col_names:
        final_dict[col_name] = dict_table[col_name]
    return final_dict


def concat(dict_table1: dict[str, list[str]], dict_table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce new column-based table with two combined column based tables."""
    final_dict = {}
    for key in dict_table1:
        final_dict[key] = dict_table1[key]

    for key in dict_table2:
        if key in final_dict:
            final_dict[key] = final_dict[key] + dict_table2[key]
            
        else:
            final_dict[key] = dict_table2[key]
            
    return final_dict


def count(values: list[str]) -> dict[str, int]:
    """Produce dict where each key has unique value in list and each value is a count of the number of times that value appears."""
    final_dict = {}
    for value in values:
        if value in final_dict:
            final_dict[value] = final_dict[value] + 1
        else:
            final_dict[value] = 1

    return final_dict
