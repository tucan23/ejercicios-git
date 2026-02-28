time=int(input("please enter the time in seconds:"))
time1=time//3600
if time1<10:
    print("the time left to 10min is:", (36000-time), "seconds")
elif time1>10:
    print("the biggest")
elif time1==10:
    print("Equal")