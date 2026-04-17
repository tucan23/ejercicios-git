import csv


header=["Name", "Section", "Spanish", "English", "Social Studies", "Science", "Average"]

def store_actual_csv(path, list1):
    new_list={}
    new_list["Name"]=list1.name
    new_list["Section"]=list1.section
    new_list["Spanish"]=list1.spanish
    new_list["English"]=list1.english
    new_list["Social Studies"]=list1.socialstudies
    new_list["Science"]=list1.science
    with open(path, "a") as file:
        writer=csv.DictWriter(file, header)
        writer.writerows(new_list)

def store_new_file(path, list1):
    with open(path, "w") as file:
        writer=csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(list1)

def store_actual_csv2(path, list1):
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
    filepath=input("enter a name for the file(without.csv)?:")
    new_file=filepath+".csv"
    return new_file   