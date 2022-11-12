import csv


def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      A list of strings corresponding to the field names in 
      the given CSV file.
    """
    table=[]
    with open(filename,'r') as csv_file:
        csv_reader=csv.DictReader(csv_file,delimiter=separator,quotechar=quote)
        table.extend(csv_reader.fieldnames)        
    return table


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """    
    list_of_dict=[]
    with open(filename,'r') as csv_file:
        csv_reader=csv.DictReader(csv_file,delimiter=separator,quotechar=quote)
        for line in csv_reader:
            list_of_dict.append(line)
            
    return list_of_dict


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    
    dict_of_values = {}
    with open(filename, newline='') as csv_file:
        reader = csv.DictReader(csv_file,
                                delimiter=separator,
                                quotechar=quote)
        for row in reader:
            temp_dict = {}
            for name in row:
                temp_dict[name] = row[name]
            dict_of_values[row[keyfield]] = temp_dict
            
    return dict_of_values


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                         delimiter=separator,
                                         quotechar=quote,
                                         quoting=csv.QUOTE_NONNUMERIC)        
        writer.writeheader()
        for value in table:
            writer.writerow({fieldnames[0]: value[fieldnames[0]],
                             fieldnames[1]: value[fieldnames[1]],
                             fieldnames[2]: value[fieldnames[2]],
                             fieldnames[3]: value[fieldnames[3]],
                             fieldnames[4]: value[fieldnames[4]]})       

