# Code to print number of records using INNER JOIN in SQL
import pandas as pd

from constants import input_table_one, input_table_two


def return_inner_join_results(table_one, table_two):
    """This method illustrates how INNER JOIN Works internally in SQL

    Inner joins combine records from two tables whenever there are matching
    values in a field common to both tables. You can use INNER JOIN with the
    Departments and Employees tables to select all the employees in each department.
    """
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

    table_data = pd.DataFrame(items)
    print(table_data)


return_inner_join_results(input_table_one, input_table_two)
