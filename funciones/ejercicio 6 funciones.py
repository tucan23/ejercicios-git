def count_upper():
    word=input("enter the sentence: ")
    count1=0
    count2=0
    for chart in word:
        if chart.isupper():
            count1 += 1
        elif chart.islower():
            count2 += 1
    return (count1,count2)

#bloque principal
(count1,count2)=count_upper()
print("number of upper case letters:", count1, "number of lower cases letters:" , count2)