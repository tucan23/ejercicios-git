employees= [
    {"name":"Robin","email":"robin@goingmerry.com","department":"Navigation",},
    {"name":"Zoro","email":"zoro@goingmerry.com","department":"Captain",}, 
    {"name": "Sanjif","email":"sanjif@goingmerry.com", "department":"Cooking",},
    {"name":"Nami","email":"nami@goingmerry.com", "department":"Navigation",},
    {"name":"Lufy","email":"lufy@goingmerry.com","department":"Captain",}
        ]
departments={}
new_name=0
new_department=0
for dept in range(len(employees)):
    new_department=employees[dept]["department"]
    new_name=employees[dept]["name"]
    if departments.get(new_department)!=None:
        new_name = departments.get(new_department)+ ", " + new_name
        #print(departments.get("new_department"))
    departments[new_department]=new_name
print(departments)

