import csv
filepath = '/Users/saikrishna/PycharmProjects/100DaysOfPython/Business-employment-data-september-2022-quarter-csv.csv'

with open(filepath,'r') as file:
    csvreader = csv.DictReader(file)
    for char in csvreader:
        print(char.get('Period'))