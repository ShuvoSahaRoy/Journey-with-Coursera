import csv
csv.register_dialect('emDialect',skipinitialspace= True,strict = True)

#part 1
def read_employees(csv_file_location):
    employee_file = csv.DictReader(open(csv_file_location),dialect='emDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list
employee_list= read_employees('E:/codes/python/Using Python to Interact with the Operating System/week 2/employees.csv')
print(employee_list)
# part 2
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data
dictionary = process_data(employee_list)
print(dictionary)
# part 3
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()
# write_report(dictionary, '/home/student-01-5b3e2ae2a518/test_report.txt')
write_report(dictionary, 'E:/codes/python/Using Python to Interact with the Operating System/week 2/test_report.txt')