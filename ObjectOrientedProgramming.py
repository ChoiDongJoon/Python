class Car():
    wheels = 4
    doors = 4
    windows = 4
    seats = 4
    def start(self):
        print(self.doors)
        print("I started") #method는 class 안에 있는 function
#파이썬은 모든 method의 첫번째 argument는 method를 호출하는 instance 자신.
    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")


#instance
porche = Car(color = "Green", price = "$40")
porche.color = "Red"
porche.start()
print(porche.color, porche.price)

ferrari = Car()
ferrari.color = "Yellow"
print(ferrari.color, ferrari.price)

mini = Car()
mini.color = "White"

print(dir(Car)) #class안의 모든 것들을 보여줌. 이미 있던 것들 override 가능

