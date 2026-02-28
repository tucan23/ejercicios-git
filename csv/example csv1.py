import csv

def read_csv(path):
    with open(path, "r") as file:
        reader= csv.DictReader(file)
        for row in reader:
            print(row)


#bloque principal
read_csv("example niños.csv")
