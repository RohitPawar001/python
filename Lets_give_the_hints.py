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


######## declare the newtype of the variable #########
from typing import NewType

name_type = NewType("name_type",str) # declared vartype as U

def names(name : name_type) -> name_type:
    return name

print(names("ram"))


############### unpacking ##########
from typing import TypedDict, Unpack

def movie_rating(Typedict):
    name:str
    reting:int
    
def rateMovie(**kwargs:Unpack[movie_rating]) -> Unpack[movie_rating]:
    return kwargs

print(rateMovie(name="a",rating=1))


