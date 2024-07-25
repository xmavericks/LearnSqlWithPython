input_table_one = [1, 1, 1, 2, 3, 3, 3]
input_table_two = [1, 1, 2, 2, 4, 'null']

cross_join_table_one = [1, 4, 5, 6, 7, 8, 9]
cross_join_table_two = [2, 3, 'null', 4, 'null']

natural_join_table_one_same_column = dict(id=[1, 1, 1, 2, 3, 3, 3])
natural_join_table_two_same_column = dict(id=[1, 1, 2, 2, 4, 'null'])

natural_join_table_one_diff_column = dict(column_table_one=[1, 1, 1, 2, 3, 3, 3])
natural_join_table_two_diff_column = dict(column_table_two=[1, 1, 2, 2, 4, 'null'])
