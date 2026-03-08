from data import store_actual_csv, read_csv, store_new_csv, store_actual_csv2,enter_path
student_list=[]

def enter_info():
    student_list.clear()
    while True:
        student={}
        name=input("enter full name of the student:")
        student["Name"]=name.capitalize()
        #enter student section
        section=input("enter the section of the student(Example:2B):") 
        student["Section"]=section.capitalize()
        #enter spanish score
        spanish=input("enter the spanish score:")
        if is_number(spanish) and validate_score(spanish):
            student["Spanish"]=spanish
        #enter english score
        english=input("enter the english score:")
        if is_number(english) and validate_score(english):
            student["English"]=english
        #enter social studies score
        socialstudies=input("enter the s. studies score:")
        if is_number(socialstudies) and validate_score(socialstudies):
            student["Social Studies"]=socialstudies
        #enter science score
        science=input("enter the science score:")
        if is_number(science) and validate_score(science):
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
    print("do you wish to:")
    print("1.work on an existing file?")
    options=int(input("2. create a new file:"))
    if options==1:
        new_file=enter_path()
        store_actual_csv(new_file,student_list)
        print("the info has been stored in",new_file)
    elif options==2:
        new_file=enter_path()
        store_new_csv(new_file,student_list)
        print("your csv has been created and the information saved")
    input("\nPress return to go back to menu...")

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
    new_file=enter_path()
    student=read_csv(new_file)
    for x in student:
        summ=int(x["Spanish"])+int(x["English"])+int(x["Social Studies"])+int(x["Science"])
        average["Name"]=x["Name"]
        x["Average"]=float(summ/4)
        #print(x)
    store_actual_csv2(new_file,student)
    return new_file

def top_3(new_file):
    average=[]
    average=read_csv(new_file)
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
    new_file=enter_path()
    average=read_csv(new_file)
    for x in average:
        summ+=float(x["Average"])
        ov_average=summ/len(average)
    print("the overall average is:", ov_average)
    input("\nPress return to go back to menu...")




def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        print("enter a valid number")
    
def validate_score(number):
        number1=0
        number1=int(number)
        if 0<=number1<=100:
            return True
        else:
            raise ValueError("enter a valid score")
        