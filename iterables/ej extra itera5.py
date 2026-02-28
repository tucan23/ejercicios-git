list1=[]
new_list=[]
for index in range(5):
    words=input("enter the words:")
    list1.append(words)

for index in range(len(list1)):
    if len(list1[index])>=4:
        new_list.append(list1[index])
print("the new list is with 4 or more words is:", new_list)