def ReadCSV(csv_file):
    """ Read an .csv file and turn it in to a matrix. """
    file_object = open(csv_file, 'r')
    content = file_object.readlines()
    print(content)
    table = []
    for line in table:
        line = line.replace("\n", "")
        line = line.split(",")
        table.append(line)

    print(table)
    return table

