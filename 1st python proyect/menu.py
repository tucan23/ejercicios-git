from actions import enter_info, print_info, store, print_csv, average, top_3, overall_average, validate_student, delete_student, failed_students

def menu():
    number=0
    yes=""
    while True:
        students=[]
        student=[]
        new_file=""
        print("*"*100)
        print("-"*100)
        print("Students database. Please choose an option:")
        print("1.Student information")
        print("2.See all information")
        print("3.Top 3 students with best average score ")
        print("4.Overall Average" )
        print("5.Export to a CSV file")
        print("6.Import CVS file")  
        print("7.Delete information")      
        try:
            number=int(input("Select a number from the menu(0 to stop):"))
        except ValueError:
            print("invalid character")
        print("*"*100)
        print("-"*100)
        if number==1:
            students=enter_info()
        if number==2:
            print_info()
        if number==3:
            average()
            top_3()
        if number==4:
            overall_average()
        if number==5:
            store()
        if number==6:
            print_csv()
        if number==7:
            validate_student()
        if number==8:
            failed_students()
        try:
            if number>9 or number.isalpha():
                print("invalid number")
        except:
            ValueError("number is not an option")
        
    
        
    


menu()

