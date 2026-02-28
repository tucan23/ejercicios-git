price=int(input("please enter the price of the product:"))
if price<100:
    print("the discount is:", price*0.02)
    print("the final price is:", price-price*0.02)
elif price>=100:
    print("the discount is:", price*0.1)
    print("the final price is:", price-price*0.1)