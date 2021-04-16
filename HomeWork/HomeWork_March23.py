class CarClass:
    wheels = 4
    model = "Some"
    speed = 10

    def set(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def about(self):
        print(self.wheels, self.model, self.speed)


car1 = CarClass()
car2 = CarClass()
car1.set(4, "BMW", 60)
car2.set(4, "Tesla", 80)
car1.about()
car2.about()


class TemplateClass:  # create empty class
    pass


car3 = TemplateClass()  # create two objects
car4 = TemplateClass()
car4.NewValue = 5
print(car4.NewValue)


# ============================================

class Person:
    def __init__(self):
        self.name = 'John'

    def pr(self, year):
        print(self.name, year)


John = Person()
John.pr(40)


# ============================================

class Car:
    wheels = 4
    model = "Some"
    speed = 123.5

    def set(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def getAll(self):
        print("Автомобиль", self.model, "может ехать со скоростью", self.speed, "на всех", self.wheels, "колесах!")


class Bike(Car):
    def __init__(self):
        self.engine = 'Powerful'

    def set_bike(self, engine):
        pass

    def getAll(self):
        print("Мотоцикл", self.model, " с двигателем " + str(self.engine) + " может ехать со скоростью", self.speed,
              "на всех", self.wheels, "колесах!")


car1 = Car()
car2 = Car()
car1.set(4, 'Toyota', 90)
car2.set(4, 'Nissan', 100)
car1.getAll()
car2.getAll()
bike1 = Bike()
bike1.set(2, 'Harley Davidson', 200)
bike1.set_bike('Powerful')
bike1.getAll()


# ============================================

class Car7:
    wheels = 4
    model = "RAM"
    speed = 123.5

    def set(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def __getAll(self):
        print("Автомобиль", self.model, "может ехать со скоростью", self.speed, "на всех", self.wheels, "колесах!")

    def info(self):
        self.__getAll()


c = Car7()
c.info()


# ============================================

class CarClass:
    def __init__(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def about(self):
        print(self.wheels, self.model, self.speed)


car1 = CarClass(4, "Volvo", 70)
car2 = CarClass(4, "Fiat", 75)
car1.about()
