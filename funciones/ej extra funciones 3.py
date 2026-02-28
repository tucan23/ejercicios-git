def vocals():
    word=input("enter the word:")
    count=0
    for f in range(len(word)):
        if word[f]=="a" or word[f]=="e" or word[f]=="i" or word[f]=="u" or word[f]=="o":
            count=count+1
    return count

#bloque principal
print("number of vocals:", vocals())
