class Car():
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
    def __str__(self):
        return f"Car with {self.wheels} wheels"
    
class Convertible(Car): #extending
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time",10)
    #super는 부모클래스를 호출하는 함수 
    """ def __init__(self, **kwargs):
        self.time = kwargs.get("time",10) -> override라서 wheels doors ... 사용 불가"""
    def take_off(self):
        return "taking off"

    def __str__(self): #override (재정의)
        return f"Car with no roof" 
    
#instance
porche = Convertible(color = "Green", price = "$40")
porche.color = "Red"
porche.start()
print(porche.color, porche.price)
porche.take_off()


mini = Car()
mini.color = "White"

print(dir(Car)) #class안의 모든 것들을 보여줌. 이미 있던 것들 override 가능

