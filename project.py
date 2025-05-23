"""
Week 3 practice project template for Python Data Analysis
Reading and writing CSV files using lists
"""


import csv



#########################################################
# Part 1 - Week 3



def print_table(table):
    """
    Echo a nested list to the console
    """
    for row in table:
        print(row)


def read_csv_file(file_name):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated CSV file
    Output: Lists of lists consisting of the fields in the CSV file
    """
    nested_list = []
    with open(file_name, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            nested_list.append(row)
    return nested_list


def write_csv_file(csv_table, file_name):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated CSV file with the name file_name
    """
    with open(file_name, 'w', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in csv_table:
            csvwriter.writerow(row)
    return file_name


# def test_part1_code():
#     """
#     Run examples that test the functions for part 1
#     """
    
#     # Simple test for reader and writer
#     test_table = read_csv_file("test_case.csv")  # create a small CSV for this test
#     print(test_table)
#     print_table(test_table)
#     print()
#     write_csv_file(test_table, "table_written.csv")

#     # Test the writer
#     cancer_risk_table = read_csv_file("cancer_risk05_v4_county.csv")
#     write_csv_file(cancer_risk_table, "cancer_risk05_v4_county_copy.csv")
#     cancer_risk_copy = read_csv_file("cancer_risk05_v4_county_copy.csv")
    
#     # Test whether two tables are the same
#     for row in range(len(cancer_risk_table)):
#         for col in range(len(cancer_risk_table[0])):
#             if cancer_risk_table[row][col] != cancer_risk_copy[row][col]:
#                 print("Difference at"), row, col, cancer_risk_table[row][col], cancer_risk_copy[row][col]
           

# test_part1_code()


#########################################################
# Part 2 - Week 4


def select_columns(my_table, col_indices):
    """
    Input: Nested list my_table and a list of integers col_indices
    Output: Nested list corresponding to sub-table formed by
    columns in col_indices
    """
    nested_list = []
    for row in my_table:
        select_list = [row[col] for col in col_indices]
        nested_list.append(select_list)
    return nested_list


def sort_by_column(my_table, col_idx):
    """
    Input: Nested list my_table and an integer col_idx
    Action: Mutate the order of the rows in my_table such that the entries in
    the column col_idx appear in DESCENDING order when interpreted as numbers
    """
    my_table.sort(key=lambda row: float(row[col_idx]), reverse = True)
    return my_table

       
def test_part2_code():
    """
    Run examples that test the functions for part 2
    """
    
    # # Load a simple example table
    # test_table = read_csv_file("test_case.csv")  # file is available at ...
    # print_table(test_table)
    # print()
    
    # # Simple test for column trimmng function
    # print_table(select_columns(test_table, [0, 2]))
    # print()
    
    # # Simple test for column sorting function
    # sort_by_column(test_table, 3)
    # print_table(test_table)
    # print()

    # Read cancer-risk data set, select columns A, B, C, E, and L, then sort by column E in descending order
    cancer_risk_table = read_csv_file("cancer_risk05_v4_county.csv")
    col_indices = [0, 1, 2, 4, 11]
    trimmed_risk_table = select_columns(cancer_risk_table, col_indices)
    sort_by_column(trimmed_risk_table, 4)
    write_csv_file(trimmed_risk_table, "cancer_risk_trimmed.csv")
    
    # Load our file "cancer_risk_trimmed_solution.csv" and compare with your solution
    trimmed_risk_solution = read_csv_file("cancer_risk_trimmed_solution.csv")
    for row in range(len(trimmed_risk_table)):
        for col in range(len(trimmed_risk_table[0])):
            if trimmed_risk_table[row][col] != trimmed_risk_solution[row][col]:
                print("Difference at"), row, col, trimmed_risk_table[row][col], trimmed_risk_solution[row][col]
    

test_part2_code()

#Output from test_part2_code()
##['1', '2', '3', '4']
##['5', '6', '7', '8']
##['-2', '-3', '-4', '-5']
##
##['1', '3']
##['5', '7']
##['-2', '-4']
##
##['5', '6', '7', '8']
##['1', '2', '3', '4']
##['-2', '-3', '-4', '-5']

    