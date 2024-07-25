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
    data_list_table_one = []
    data_list_table_two = []
    for item in table_one:
        for ele in table_two:
            if item == ele:
                data_list_table_one.append(ele)
                data_list_table_two.append(ele)

    for item in table_one:
        if item not in table_two:
            data_list_table_one.append(item)
            data_list_table_two.append('null')

    items = {
        "table_one_updated_result": data_list_table_one,
        "table_two_updated_result": data_list_table_two
    }

    table_data = pd.DataFrame(items)
    print(table_data)


return_left_join_results(input_table_one, input_table_two)
