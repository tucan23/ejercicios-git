from actions import enter_info, print_info, store, print_csv, average, top_3, overall_average

def menu():
    number=1
    while number!=0:
        students=[]
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
            new_file=average()
            top_3(new_file)
        if number==4:
            overall_average()
        if number==5:
            store()
        if number==6:
            print_csv()
        if number>6:
            raise ValueError("number is not an option")
        
    
        
    


menu()

