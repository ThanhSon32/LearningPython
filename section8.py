# Exercise 1:
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model =model

    def start_engine(self):
        return f"{self.brand} {self.model} engine started!"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def start_engine(self):
        return f"{self.brand} {self.model} is now running silently on battery"

car1 = Car('Toyota', 'Corolla')
car2 = ElectricCar("Tesla", "Model 3", "75 kWh")

print (car1.start_engine())
print (car2.start_engine())

# Exercise 2:
class Book():
    def __init__(self, tittle, author, pages):
        self.tittle = tittle
        self.author = author
        self.pages = pages

b = Book('Python Rock', 'Jose', 200)
print(b)

# Exercise 3:
class Book2():
    def __init__(self, tittle, author, pages):
        self.tittle = tittle
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.tittle} by {self.author}"
    def __len__(self):
        return self.pages

b2 = Book2('Python Rock', 'Jose', 200)

print(str(b2))
print(len(b2))