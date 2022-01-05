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

