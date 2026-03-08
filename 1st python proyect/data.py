import csv

header=["Name", "Section", "Spanish", "English", "Social Studies", "Science", "Average"]

def store_actual_csv(path, list1):
    with open(path, "a") as file:
        writer=csv.DictWriter(file, header)
        writer.writerows(list1)

def store_actual_csv2(path, list1):
    with open(path, "w") as file:
        writer=csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(list1)

def store_new_csv(path, list1):
    with open(path, "a") as file:
        writer=csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(list1)

def read_csv(path):
    student=[]
    with open(path, "r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            student.append(row)
    return student

def enter_path():
    filepath=""
    filepath=input("which file do you want to open(without.csv)?:")
    new_file=filepath+".csv"
    return new_file   