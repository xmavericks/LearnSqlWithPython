# Code to print number of records using LEFT JOIN in SQL
import pandas as pd

from constants import input_table_one, input_table_two, scenario_table_one, scenario_table_two


def return_left_join_results(table_one, table_two):
    """This method illustrates how LEFT JOIN Works internally in SQL

    Definition: SQL LEFT JOIN, also known as a LEFT OUTER JOIN, is a
    type of SQL JOIN operation that retrieves all records from the
    left table (table1) and the matching records from the right table (table2).
    If there are no matching records in the right table, NULL values are included for those columns.
    """
    # INNER JOIN
    data_list_table_one = []
    data_list_table_two = []
    for item in table_one:
        for ele in table_two:
            if item == ele and ele != 'null':
                data_list_table_one.append(ele)
                data_list_table_two.append(ele)

    # ADDITIONAL ELEMENTS OF LEFT TABLE NOT PRESENT IN RIGHT TABLE
    for item in table_one:
        if item not in table_two or item == 'null':
            data_list_table_one.append(item)
            data_list_table_two.append('null')

    items = {
        "table_one_updated_result": data_list_table_one,
        "table_two_updated_result": data_list_table_two
    }

    return items


print("-------------------------------- Scenario : 1 ----------------------------------------\nWhen Tables are: \n")
print(f"Table One: {input_table_one}")
print(f"Table Two: {input_table_two}\n")
tables = return_left_join_results(input_table_one, input_table_two)
table_data = pd.DataFrame(tables)
print(table_data)

print("\n-------------------------------- Scenario : 2 ----------------------------------------\nWhen Tables are: \n")
print(f"Table One: {scenario_table_one}")
print(f"Table Two: {scenario_table_two}\n")
scenario_tables = return_left_join_results(scenario_table_one, scenario_table_two)
scenario_table_data = pd.DataFrame(scenario_tables)
print(scenario_table_data)


# Output Results
"""
-------------------------------- Scenario : 1 ----------------------------------------
When Tables are: 

Table One: [1, 1, 1, 2, 3, 3, 3]
Table Two: [1, 1, 2, 2, 4, 'null']

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

-------------------------------- Scenario : 2 ----------------------------------------
When Tables are: 

Table One: [1, 1, 1, 1, 1, 'null', 'null']
Table Two: [1, 1, 1, 2, 'null']

   table_one_updated_result table_two_updated_result
0                         1                        1
1                         1                        1
2                         1                        1
3                         1                        1
4                         1                        1
5                         1                        1
6                         1                        1
7                         1                        1
8                         1                        1
9                         1                        1
10                        1                        1
11                        1                        1
12                        1                        1
13                        1                        1
14                        1                        1
15                     null                     null
16                     null                     null
"""
