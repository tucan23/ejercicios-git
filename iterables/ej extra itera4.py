list1=[5,6,9,8,6,4,2,1]
over_average=[]
average=0
sum=0
for index in range(len(list1)):
    sum +=list1[index]
    
average=sum//index
print("the average is:", average)

for index in range(len(list1)):
    if list1[index]>=average:
        over_average.append(list1[index])
print("list of numbers over average", over_average)