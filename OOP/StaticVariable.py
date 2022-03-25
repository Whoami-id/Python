class Car():
    price = "expensive"


c = Car()
print(c.price)

print(Car.price)

Car.price = "cheep"
print(c.price)

print(Car.price)
