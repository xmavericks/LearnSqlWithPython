# Code to print number of records using CROSS JOIN in SQL
import pandas as pd

from constants import cross_join_table_one, cross_join_table_two


def return_cross_join_results(table_one, table_two):
    """This method illustrates how CROSS JOIN Works internally in SQL

    Definition: A cross join is a type of join that returns the Cartesian product of rows from the tables in the join.
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

    return items


tables = return_cross_join_results(cross_join_table_one, cross_join_table_two)
table_data = pd.DataFrame(tables)
print(table_data)


# Output Results : Total records using cross join is (no_of_records in left table * no_of_records in right table)
# Check respective tables in constants.py file and compare with output results below
"""
    table_one_updated_result table_two_updated_result
0                          1                        2
1                          1                        3
2                          1                     null
3                          1                        4
4                          1                     null
5                          4                        2
6                          4                        3
7                          4                     null
8                          4                        4
9                          4                     null
10                         5                        2
11                         5                        3
12                         5                     null
13                         5                        4
14                         5                     null
15                         6                        2
16                         6                        3
17                         6                     null
18                         6                        4
19                         6                     null
20                         7                        2
21                         7                        3
22                         7                     null
23                         7                        4
24                         7                     null
25                         8                        2
26                         8                        3
27                         8                     null
28                         8                        4
29                         8                     null
30                         9                        2
31                         9                        3
32                         9                     null
33                         9                        4
34                         9                     null
"""
