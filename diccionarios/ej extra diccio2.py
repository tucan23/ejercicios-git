sale=[
    {"date" : "19/'1/26","customer_email" : "conesinawaffle@coneiw.com", 
    "item" :
        [
        {"name" : "cones","upc":"C5","unit_price":"2",},
        {"name" : "ny_cookie","upc": "N3" ,"unit_price":"3",},
        {"name": "cupcake","upc": "C2","unit_price":"2",},
        {"name": "eclaire","upc": "E1","unit_price":"2",},
        ]
    },
    {"date" : "22/'1/26","customer_email" : "frenchbakerse@frenchie.com", 
    "item" :
        [ 
        {"name" : "ny_cookie","upc": "N3" ,"unit_price":"5",},
        {"name": "eclaire","upc":"E1", "unit_price":"8",},
        ]
    },
    {
    "date" : "22/'1/26","customer_email" : "frenchbakerse@frenchie.com", 
    "item" :  
        [
        {"name" : "cones","upc":"C5","unit_price":"5",},
        {"name" : "ny_cookie","upc":"N3" ,"unit_price":"6",},
        ]
    }]
saleupc={}
upc=0
unit_price=0
for daily_sales in range(len(sale)):
    for bakery in range(len(sale[daily_sales]["item"])):
        upc=sale[daily_sales]["item"][bakery]["upc"]
        unit_price=int(sale[daily_sales]["item"][bakery]["unit_price"])
        if saleupc.get(upc)!=None:
            unit_price= saleupc.get(upc)+unit_price
        saleupc[upc]=unit_price
print(saleupc)
#print(saleupc)

