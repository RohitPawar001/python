##################################

def greet(name:str) -> str:
    return f"hi {name}"

greeting = greet("Ziyang")
print(greeting)
# op - hi Ziyang

##################################

from typing import List

names_list : List[str] = []

for i in range(int(input("enter the no of names to add the list"))):
    name = input("enter the name")
    names_list.append(name)
    
print(names_list)

