list1=[]
max_value=0
index=0
while index<=10:
    number=int(input("enter the 10 numbers:"))
    list1.append(number)
    if list1[index]>max_value:
        max_value=list1[index]
    index +=1

print("values on the list:", list1, "maximum value:", max_value)