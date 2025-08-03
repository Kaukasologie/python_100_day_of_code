# *args - Positional Variable-Length Arguments
def add(*args):
    print(f"Access to any argument: {args[2]}")
    sum = 0
    for n in args:
        sum += n
    print(f"The sum of the arguments specified via args: {sum}\n")

add(3, 5, 6, 2, 1, 7, 4, 3)


# **kwargs - Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(f"kwargs: {kwargs}")
    for key, value in kwargs.items():
        print(f"key: {key}")
        print(f"value: {value}\n")
    n += kwargs["add"]          # 2
    n *= kwargs["multiply"]     # 5
    print(n)

calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
