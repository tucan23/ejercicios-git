import json

def ask_help(path):
    pokedex=[]
    with open(path, "r") as file:
        pokedex=json.load(file)
        return pokedex
    

def print_pokemon(pokedex):
    #print(pokedex)
    for pokemon in pokedex:
        print("name:",pokemon["name"]["english"])
        print("Attack:", pokemon["base"]["Attack"])
        print("Defense", pokemon["base"]["Defense"])
        print("Speed:", pokemon["base"]["Speed"])
        print("_" *20)
        

def main():
    pokedex=[]
    pokedex=ask_help("pokedex.json")
    print_pokemon(pokedex)



main()