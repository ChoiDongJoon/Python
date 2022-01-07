a = 2
b = 3
c = False
print(a + b)
d = None

day_list = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(type(day_list))
print(day_list[3])
day_list.append("Sat")
print(day_list)
day_tuple = ("Mon", "Tue", "Wed", "Thur", "Fri")
print(type(day_tuple))

dongjun = {
    "name" : "dongjun",
    "age" : 23,
    "korean" : True
    }
print(dongjun)
dongjun["handsome"] = True
print(dongjun)

def say_Hello(who): 
    print("Hello", who)
say_Hello("Dongjun")

def say(name, age) :
    return f"Hello {name} you are {age} years old"
hello = say("dongjun", "23")
print(hello)

def plus(a, b):
    if type(b) is int or type(b) is float:
        return a+b
    else:
        return None
print(plus(12, 1.2))
print(plus(12, "1.2"))

def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you cant drink")
    elif age == 18:
        print("you are new to this!")
    else:
        print("enjoy your drink")

age_check(19)
age_check(18)
age_check(17)


days = ["Mon", "Tue", "Wed", "Thur", "Fri"]

for day in days:
    print(day)

import math

print(math.ceil(1.2))
print(math.fabs(-1.2))

from math import ceil, fsum






