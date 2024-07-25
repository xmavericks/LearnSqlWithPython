# Code to print number of records using INNER JOIN in SQL
import pandas as pd

from constants import input_table_one, input_table_two


def return_inner_join_results(table_one, table_two):
    """This method illustrates how INNER JOIN Works internally in SQL

    Inner joins combine records from two tables whenever there are matching
    values in a field common to both tables. You can use INNER JOIN with the
    Departments and Employees tables to select all the employees in each department.
    """
    # INNER JOIN
    data_list_table_one = []
    data_list_table_two = []
    for item in table_one:
        for ele in table_two:
            if item == ele:
                data_list_table_one.append(ele)
                data_list_table_two.append(ele)
    items = {
        "table_one_updated_result": data_list_table_one,
        "table_two_updated_result": data_list_table_two
    }

    return items


tables = return_inner_join_results(input_table_one, input_table_two)
table_data = pd.DataFrame(tables)
print(table_data)

# Output results : Total number of records is last_id + 1 i.e, 8
"""
   table_one_updated_result  table_two_updated_result
0                         1                         1
1                         1                         1
2                         1                         1
3                         1                         1
4                         1                         1
5                         1                         1
6                         2                         2
7                         2                         2
"""
