from data import store_actual_csv, read_csv, store_new_file, store_actual_csv2,enter_path
student_list=[]
import csv

def enter_info():
    student_list.clear()
    while True:
        student={}
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
                student["Name"]=letter
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
                        student["Section"]=section1
                        break
            elif count1==2:
                    if section[0].isdigit() and section[1].isalpha():
                        section1=section[0]+section[1].capitalize()
                        student["Section"]=section1
                        break
            else:
                    print("please enter a valid section(2A, 11B, etc)")
        #enter spanish score
        spanish=input("enter the spanish score:")
        if is_number(spanish):
            student["Spanish"]=spanish
        #enter english score
        english=input("enter the english score:")
        if is_number(english):
            student["English"]=english
        #enter social studies score
        socialstudies=input("enter the s. studies score:")
        if is_number(socialstudies):
            student["Social Studies"]=socialstudies
        #enter science score
        science=input("enter the science score:")
        if is_number(science):
            student["Science"]=science
        student_list.append(student)
        yes=input("Do you want to add another student(y/n)?:")
        if yes=="n" or yes=="N":
            break
        if yes=="y" or yes=="Y":
            continue
        else:
            raise ValueError("please enter y or n")
    return student_list

    
def print_info():
    print("Student information:")
    #print(student_list)
    for x in student_list:
        print("Name:",x["Name"], "Section:",x["Section"])
        print("Spanish Score:",x["Spanish"])
        print("English Score:",x["English"])
        print("Social Studies Score:",x["Social Studies"])
        print("Science Score:",x["Science"])
    input("\nPress return to go back to menu...")

def store():
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
            print(name["Name"],student["Name"])
            if name["Name"]==student["Name"] and name["Section"]==student["Section"]:
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
    else:
        #print(student)
        print("*"*100)
        for x in student:
            print("Name:",x["Name"], "Section:",x["Section"])
            print("Spanish Score:",x["Spanish"])
            print("English Score:",x["English"])
            print("Social Studies Score:",x["Social Studies"])
            print("Science Score:",x["Science"])
            input("\nPress return to see other student information...")
    input("\nPress return to go back to menu...")

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
    store_actual_csv2("chiquis.csv",student)

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
    ov_average=0
    average=read_csv("chiquis.csv")
    for x in average:
        summ+=float(x["Average"])
        ov_average=summ/len(average)
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
        if name["Spanish"]<=6 or name["English"]<=6 or name["Science"]<=6 or name["Social Studies"]<=6:
            print(name["Name"],name["Section"])
        if name["Spanish"]<=6:
            print("Science:", name["Spanish"])
            count+=1
        elif  name["English"]<=6:
            print("English:", name["English"])
            count+=1
        elif  name["Science"]<=6:
            print("Science", name["Science"])
            count+=1
        elif  name["Social Studies"]<=6:
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

        
        