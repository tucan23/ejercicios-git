count_1=0
count_2=0
count_3=0
summ=0
summ_1=0
summ_2=0
number_of_grades=int(input("enter the number of grades:"))

while count_1<number_of_grades:
    grade=int(input("please enter the grade:"))
    summ +=grade
    count_1 += 1
    if grade>=70:
        count_2 +=1
        summ_1+= grade
    elif grade<70:
        count_3 +=1
        summ_2 += grade
    
print("the general average is:", summ/count_1 )
if count_2!=0:
    print("the aprobbed grades average is:", summ_1/count_2)
if count_3!=0:
    print("the disaproved grades average is:", summ_2/count_3)

