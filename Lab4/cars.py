class Person:
    def __init__(self, name:str, surname:str, age:int):
        self.name=name
        self.surname=surname
        self.age=age

    def __str__(self):
        return f"{self.name} {self.surname} {self.age} years old"

class Driver(Person):
    def __init__(self, name: str, surname: str, age: int, experience: int):
        super().__init__(name, surname, age)
        self.experience=experience

    def __str__(self):
        return f"{super().__str__()} with {self.experience} experience"

class Engine:
    def __init__(self, power:int, company:str):
        self.power=power
        self.company=company

    def __str__(self):
        return f"power:{self.power}, company:{self.company}"

class Car:
    def __init__(self, marka:str, car_class:str, weight:int, name:str, surname:str,
                 age:int, experience:int, power:int, company:str):
        self.driver=Driver(name=name, surname=surname, age=age, experience=experience)
        self.engine=Engine(power=power, company=company)
        self.marka=marka
        self.car_class=car_class
        self.weight=weight

    def start(self) -> str:
        return f"Поехали"

    def stop(self) -> str:
        return f"Останавливаемся"

    def turn_right(self) -> str:
        return f"Поворот направо"

    def turn_left(self) -> str:
        return f"Поворот налево"

    def __str__(self):
        return f"{self.driver}, {self.engine}, marka:{self.marka}, car_class:{self.car_class}, weight:{self.weight}"

class Lorry(Car):
    def __init__(self,marka:str, car_class:str, weight:int, name:str, surname:str,
                 age:int, experience:int, power:int, company:str, carrying:int):
        super().__init__(marka=marka, car_class=car_class, weight=weight, name=name, surname=surname,
                         age=age, experience=experience, power=power, company=company)
        self.carrying=carrying

    def __str__(self):
        return f"{super().__str__()}, carrying:{self.carrying}"

class SportCar(Car):
    def __init__(self,marka:str, car_class:str, weight:int, name:str, surname:str,
                 age:int, experience:int, power:int, company:str, speed:float):
        super().__init__(marka=marka, car_class=car_class, weight=weight, name=name, surname=surname,
                         age=age, experience=experience, power=power, company=company)
        self.speed=speed

    def __str__(self):
        return f"{super().__str__()}, speed:{self.speed}"

sport_car_1=SportCar(marka="SomeMarka", car_class="SomeClass", weight=200, name="Elnur", surname="Alibaev",
                     age=19, experience=0, power=23, company="Google", speed=320)

print(sport_car_1.start())


