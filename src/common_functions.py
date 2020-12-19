import csv
import random

def read_csv(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        line = random.randint(1, 52458) #just in case I need to print the line.
        row = list(rows[line])
        return (row[0])