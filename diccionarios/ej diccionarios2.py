flavors=["straberry", "pineapple", "blueberry", "mango"]
cakes=["cupcake", "cheescake", "ice cream cake", "pancake"]
types={}
for item in range(len(cakes)):
    types[cakes[item]]=flavors[item]

print(types)
