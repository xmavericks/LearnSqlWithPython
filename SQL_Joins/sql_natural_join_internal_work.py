# Code to print number of records using NATURAL JOIN in SQL
import pandas as pd

from constants import (natural_join_table_one_same_column, natural_join_table_two_same_column,
                       natural_join_table_one_diff_column, natural_join_table_two_diff_column)


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
            if item == ele and ele != 'null':
                data_list_table_one.append(ele)
                data_list_table_two.append(ele)
    items = {
        "table_one_updated_result": data_list_table_one,
        "table_two_updated_result": data_list_table_two
    }

    table_data = pd.DataFrame(items)
    print(table_data)


def return_cross_join_results(table_one, table_two):
    """This method illustrates how CROSS JOIN Works internally in SQL

    Definition:A cross join is a type of join that returns the Cartesian product of rows from the tables in the join.
    In other words, it combines each row from the first table with each row from the second table. This article
    demonstrates, with a practical example, how to do a cross join in Power Query.
    """
    data_list_table_one = []
    data_list_table_two = []

    for item in table_one:
        for ele in table_two:
            data_list_table_one.append(item)
            data_list_table_two.append(ele)

    items = {
        "table_one_updated_result": data_list_table_one,
        "table_two_updated_result": data_list_table_two
    }

    table_data = pd.DataFrame(items)
    print(table_data)


def return_natural_join_results(table_one, table_two):
    table_one_values = list(table_one.values())[0]
    table_two_values = list(table_two.values())[0]
    if table_one.keys() == table_two.keys():
        return return_inner_join_results(table_one_values, table_two_values)
    elif table_one.keys() != table_two.keys():
        return return_cross_join_results(table_one_values, table_two_values)
    else:
        return "No Tables Found...!!!"


# With table columns different
return_natural_join_results(table_one=natural_join_table_one_diff_column, table_two=natural_join_table_two_diff_column)

# With same table columns
return_natural_join_results(table_one=natural_join_table_one_same_column, table_two=natural_join_table_two_same_column)

# Output results : Total number of records is last_id + 1 i.e, 8
"""
DIFFERENT COLUMN NAME RESULT : Similar result as Cross-Join

    table_one_updated_result table_two_updated_result
0                          1                        1
1                          1                        1
2                          1                        2
3                          1                        2
4                          1                        4
5                          1                     null
6                          1                        1
7                          1                        1
8                          1                        2
9                          1                        2
10                         1                        4
11                         1                     null
12                         1                        1
13                         1                        1
14                         1                        2
15                         1                        2
16                         1                        4
17                         1                     null
18                         2                        1
19                         2                        1
20                         2                        2
21                         2                        2
22                         2                        4
23                         2                     null
24                         3                        1
25                         3                        1
26                         3                        2
27                         3                        2
28                         3                        4
29                         3                     null
30                         3                        1
31                         3                        1
32                         3                        2
33                         3                        2
34                         3                        4
35                         3                     null
36                         3                        1
37                         3                        1
38                         3                        2
39                         3                        2
40                         3                        4
41                         3                     null
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
