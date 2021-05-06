import csv
from Utils import Dictionary

def writeInCsv():
    field_names = ['Standard', 'phyR', 'sra', 'DSL Interface']

    df = Dictionary.dict

    with open('Sample.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerow(df)