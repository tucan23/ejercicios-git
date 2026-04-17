from data import store_actual_csv, read_csv, store_new_file, store_actual_csv2,enter_path

import csv
student_list=[]

class Student:
    
    def __init__(self,name,section,spanish,english,socialstudies,science):
        self.name=name
        self.section=section
        self.spanish=spanish
        self.english=english
        self.socialstudies=socialstudies
        self.science=science
        
        
def enter_info():
        while True:
            count=1
            letter=""
            while True:
                name=input("enter full name of the student:")
                letter=""
                for chart in name:
                    if chart==" ":
                        continue
                    letter=letter+chart
                if letter.isalpha():
                    letter=""
                    for chart in name:
                            letter=letter+chart.capitalize()
                    name=letter
                    break
                else:
                    print("please enter a valid name")
        
            while True:
                count1=0
                section1=""
                section=input("enter the section of the student(Example:2B):") 
                count1=len(section)
                if count1==3:
                    if not section[0].isalpha() and not section[1].isalpha() and section[2].isalpha():
                        section1=section[0]+section[1]+section[2].capitalize()
                        section=section1
                        break
                elif count1==2:
                    if section[0].isdigit() and section[1].isalpha():
                        section1=section[0]+section[1].capitalize()
                        section=section1
                        break
                else:
                    print("please enter a valid section(2A, 11B, etc)")
        #enter spanish score
            spanish=int(input("enter the spanish score:"))
            while not is_number(spanish):
                spanish=int(input("enter the spanish score:"))
        #enter english score
            english=input("enter the english score:")
            while not is_number(english):
                english=input("enter the english score:")
        #enter social studies score
            socialstudies=input("enter the s. studies score:")
            while not is_number(socialstudies):
                socialstudies=input("enter the s. studies score:")
        #enter science score
            science=input("enter the science score:")
            while not is_number(science):
                science=input("enter the science score:")
            student_list.append(Student(name,section,spanish,english,socialstudies,science))
            yes=input("Do you want to add another student(y/n)?:")
            if yes=="n" or yes=="N":
                break
            if yes=="y" or yes=="Y":
                continue
            else:
                raise ValueError("please enter y or n")
        return student_list



def print_info(student_list):
    print("Student information:")
    #print(student_list)
    for student in student_list:
        print("Name:",student.name, "Section:",student.section)
        print("Spanish Score:",student.spanish)
        print("English Score:",student.english)
        print("Social Studies Score:",student.socialstudies)
        print("Science Score:",student.science)
    input("\nPress return to go back to menu...")

def store(student_list):
    exist=True
    print("do you wish to:")
    print("1.save on an existing file(chiquis.csv)?")
    options=int(input("2.save on a new file:"))
    if options==1:
        exist=student_exist(student_list, "chiquis.csv")
        if not exist:
            store_actual_csv("chiquis.csv",student_list)
            print("the info has been stored in chiquis.csv")
    elif options==2:
        new_file=enter_path()
        store_new_file(new_file,student_list)
        print("your csv has been created and the information saved")
    input("\nPress return to go back to menu...")

def student_exist(student_list, path):
    exist=False
    list_in_file=[]
    list_in_file=read_csv(path)
    for student in list_in_file:
        for name in student_list:
            if name(student.name)==student["Name"] and name(student.section)==student["Section"]:
                exist=True
                print("Student already on the list")
                break
        else:
            exist=False
    return exist
    

def print_csv():
    student=[]
    new_file=enter_path()
    student=read_csv(new_file)
    if not student:
        print("file is empty")
    print("file has been imported")
    input("\nPress return to go back to menu...")
    return student

def average():
    student=[]
    summ=0
    average={}
    average_list=[]
    student=read_csv("chiquis.csv")
    for x in student:
        summ=int(x["Spanish"])+int(x["English"])+int(x["Social Studies"])+int(x["Science"])
        average["Name"]=x["Name"]
        x["Average"]=float(summ/4)
        #print(x)
    store_new_file("chiquis.csv",student)

def top_3():
    average=[]
    average=read_csv("chiquis.csv")
    average.sort(key= lambda x: float(x["Average"]), reverse=True)
    print("*"*100)
    print("The top 3 averages are:")
    for x in range(3):
        print(average[x]["Name"], ":", average[x]["Average"])
    input("\nPress return to go back to menu...")

def overall_average():
    average=[]
    summ=0
    count=1
    ov_average=0
    average=read_csv("chiquis.csv")
    for x in average:
        summ+=float(x["Average"])
        count+=1
    ov_average=round(float(summ)/(count),2)
    print("the overall average is:", ov_average)
    input("\nPress return to go back to menu...")

def validate_student():
    yes=""
    student_list=[]
    student1=""
    while True:
        student=input("please enter the student name:")
        student1=student.upper()
        section=input("please enter the section:")
        if len(section)==2:
            section1=section[0]+section[1].upper()
        elif len(section)==3:
            section1=section[0]+section[1]+section[2].upper()
        student_list=read_csv("chiquis.csv")
        for name in student_list:
            print(student1,name["Name"],section1,name["Section"])
            if student1==name["Name"] and section1==name["Section"]:
                print("The student is in the list")
                yes=True
            else:
                yes=False
                print("The student is not on the list, please try again")
        break
    delete_student(student1,section1, student_list)
    

def delete_student(student1,section1,student_list):
        header=["Name", "Section", "Spanish", "English", "Social Studies", "Science", "Average"]
        yes=input("Do you want to delete the student?(y/n):")
        if yes=="y" or yes=="Y":
            with open("chiquis.csv", "w") as file:
                writer=csv.DictWriter(file,header)
                writer.writeheader()
                for name in student_list:
                    print(student1, name["Name"])
                    if student1==name["Name"] and section1==name["Section"]:
                        continue
                    else:   
                        writer.writerow(name)


def failed_students():
    student_list=[]
    count=0
    student_list=read_csv("chiquis.csv")
    print("List of failed students")
    for name in student_list:
        if float(name["Spanish"])<=6 or float(name["English"])<=6 or float(name["Science"])<=6 or float(name["Social Studies"])<=6:
            print(name["Name"],name["Section"])
        if float(name["Spanish"])<=6:
            print("Science:", name["Spanish"])
            count+=1
        elif  float(name["English"])<=6:
            print("English:", name["English"])
            count+=1
        elif  float(name["Science"])<=6:
            print("Science", name["Science"])
            count+=1
        elif  float(name["Social Studies"])<=6:
            print("Social Studies", name["Social Studies"])
            count+=1
    if count==0:
        print("There are no failed students")

                
def is_number(number):
    number1=""
    si=True
    try:
        number1=float(number)
        si=True
    except ValueError:
            print("please enter a valid score")
    try:
        if 0<=number1 and number1<=100:
            si=True
    except TypeError:
                print ("please enter a valid score")
    
    return si

        
        