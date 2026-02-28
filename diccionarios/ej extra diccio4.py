supermarket_products=[
    {"name":"milk","category": "diary","price":5},
    {"name":"cheese","category": "diary","price":5},
    {"name":"yogurt","category": "diary","price":5},    
    {"name":"cookies","category": "bread","price":5},
    {"name":"bread","category": "bread","price":5},
    {"name":"pasta","category": "bread","price":5},
    {"name":"sausages","category": "deli","price":5},
    {"name":"ham","category": "deli","price":5},
    {"name":"ground meat","category": "meat","price":5},
    {"name":"chicken thighs","category": "meat","price":5},
    ]
super_price=0
super_department=0
dictionary={}
for category1 in range(len(supermarket_products)):
        super_price=supermarket_products[category1]["price"]
        super_department=supermarket_products[category1]["category"]
        #print(super_price,super_department)
        if dictionary.get(super_department)!=None:
            new_price=dictionary.get(super_department)
            super_price= super_price + new_price
        dictionary[super_department]=super_price  
print(dictionary)



