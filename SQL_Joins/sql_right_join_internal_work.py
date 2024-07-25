# Code to print number of records using LEFT JOIN in SQL
import pandas as pd

from constants import input_table_one, input_table_two


def return_right_join_results(table_one, table_two):
    """This method illustrates how RIGHT JOIN Works internally in SQL

    Definition:Right JOIN allows to join two table, keeping all the data or right table and only matching data of left
    table. Right JOIN is a type of outer join in SQL. It allows us to deal with missing values in database and also
    helps in analyzing relationships between data.
    """
    data_list_table_one = []
    data_list_table_two = []
    for item in table_one:
        for ele in table_two:
            if item == ele:
                data_list_table_one.append(ele)
                data_list_table_two.append(ele)

    for item in table_two:
        if item not in table_one:
            data_list_table_two.append(item)
            data_list_table_one.append('null')

    items = {
        "table_one_updated_result": data_list_table_one,
        "table_two_updated_result": data_list_table_two
    }

    table_data = pd.DataFrame(items)
    print(table_data)


return_right_join_results(input_table_one, input_table_two)


# Output Results
"""
  table_one_updated_result table_two_updated_result
0                        1                        1
1                        1                        1
2                        1                        1
3                        1                        1
4                        1                        1
5                        1                        1
6                        2                        2
7                        2                        2
8                     null                        4
9                     null                     null
"""
