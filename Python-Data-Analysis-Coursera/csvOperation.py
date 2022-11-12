file = open("forCsv.csv","r")
for line in file.readlines()[1:]:
    print(line.strip())