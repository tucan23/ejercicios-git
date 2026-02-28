list1=[1,2,3,4,5,6,7,8,9,10]
index=0
while index<len(list1):
    if list1[index]%2 !=0:
        list1.pop(index)
        index -=1

    index +=1
print(list1)