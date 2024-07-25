# Code to print number of records using LEFT JOIN in SQL
import pandas as pd

from constants import input_table_one, input_table_two


def return_left_join_results(table_one, table_two):
    """This method illustrates how LEFT JOIN Works internally in SQL

    Definition:SQL LEFT JOIN, also known as a LEFT OUTER JOIN, is a
    type of SQL JOIN operation that retrieves all records from the
    left table (table1) and the matching records from the right table (table2).
    If there are no matching records in the right table, NULL values are included for those columns.
    """
    # INNER JOIN
    data_list_table_one = []
    data_list_table_two = []
    for item in table_one:
        for ele in table_two:
            if item == ele:
                data_list_table_one.append(ele)
                data_list_table_two.append(ele)

    # ADDITIONAL ELEMENTS OF LEFT TABLE NOT PRESENT IN RIGHT TABLE
    for item in table_one:
        if item not in table_two:
            data_list_table_one.append(item)
            data_list_table_two.append('null')

    items = {
        "table_one_updated_result": data_list_table_one,
        "table_two_updated_result": data_list_table_two
    }

    return items


tables = return_left_join_results(input_table_one, input_table_two)
table_data = pd.DataFrame(tables)
print(table_data)


# Output Results
"""
    table_one_updated_result table_two_updated_result
0                          1                        1
1                          1                        1
2                          1                        1
3                          1                        1
4                          1                        1
5                          1                        1
6                          2                        2
7                          2                        2
8                          3                     null
9                          3                     null
10                         3                     null
"""
