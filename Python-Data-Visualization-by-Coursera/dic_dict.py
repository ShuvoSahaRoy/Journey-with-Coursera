import csv

def read_csv_file(file_name, separator, quote):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Nested list consisting of the fields in the CSV file
    """

    with open(file_name, newline='') as csv_file:
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=separator, quotechar=quote)
        for row in csv_reader:
            csv_table.append(row)
    return csv_table

