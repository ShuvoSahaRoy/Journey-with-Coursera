import csv


def read_csv_fieldnames(filename, separator, quote):
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator,
                                   quotechar=quote)
    return csvreader.fieldnames


def read_csv_as_list_dict(filename, separator, quote):
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator,
                                   quotechar=quote)
        list_dict = []
        for row in list(csvreader):
            list_dict.append(row)
    return list_dict


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator,
                                   quotechar=quote)
        dic_dict = {}
        for row in csvreader:
            dic_dict[row[keyfield]] = row
    return dic_dict


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    with open(filename, 'w', newline='') as csvfile:
        csv_w = csv.DictWriter(csvfile, fieldnames, delimiter=separator, quotechar=quote)
        csv_w.writeheader()
        for row in table:
            csv_w.writerow(row)
    return csvfile
