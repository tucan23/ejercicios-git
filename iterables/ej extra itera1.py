list1=[]
number=1
count=0
while number!=0:
    number=int(input(" enter the numbers on the list(to stop press 0):" ))
    list1.append(number)

new_number=int(input("enter a new number:"))

for index in range(len (list1)):
    if list1[index]==new_number:
        count +=1
    
print("the number", new_number, "appears", count, "times in the list")