from os import system as execute 
from CSVParser import ReadCSV
from HistoryParser import ReadHistoryContent
from SpecificComparators import FloatComparator

# 1. Download the newest .csv data
execute("rm cases-brazil-total.csv")
execute("wget https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-total.csv")

# 2. Make the .csv readable
csv_table = ReadCSV("cases-brazil-total.csv")

# 3. Split data and parameters
parameters = csv_table[0]
data = csv_table[1]

# 4. Read content of history.txt
history_content = ReadHistoryContent("history.txt")

# 5. Compare .csv with history.txt
diferences = FloatComparator(history_content, data)

# 6. Finnaly, show the data.
print("*** Covid19 Relatory ***")
for index in len(range(parameters)):
    print(f"   * [parameters[index]] >>> [data[index]] ~ (diferences[index])")
