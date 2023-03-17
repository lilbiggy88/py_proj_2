import csv
from abc import ABC, abstractmethod
from pprint import pprint

def read_csv(file):
    with open("sample.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

read_csv("sample.csv")

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader


# class Cupcake:
#     def __init__(self, name, price, flavor, frosting, filling):
#         self.name = name
#         self.price = price
#         self.flavor = flavor
#         self.frosting = frosting
#         self.filling = filling
#         self.sprinkles = []
#         # self.sprinkles = sprinkles
    
#     # def my_method(self):
#     #     pass
#     def add_sprinkles(self, *args):
#         for sprinkle in args:
#             self.sprinkles.append(sprinkle)


# my_cupcake = Cupcake("Chocolate with fudge filling", 3.99, "Chocolate", "Dark Chocolate", "Fudge")

# my_cupcake.add_sprinkles('chocolate', 'blueberry', 'colored sugar')

# print(my_cupcake.sprinkles)

# # ADDING THINGS TO A CUPCAKE
# # my_cupcake.frosting = "Vanilla"
# # my_cupcake.filling = "Red Velvet"
# # my_cupcake.name = "Valentine's Cupcake"
# # my_cupcake.is_miniature = True
# # print(my_cupcake.is_miniature)

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
        return None
    
def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)
                

class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod

    def calculate_price(self, quantity):
        return quantity * self.price
    
class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

my_mini_cupcake = Mini("Chocolate", 1.99, "Chocolate", "White",)
print(my_mini_cupcake.name)
print(my_mini_cupcake.price)
print(my_mini_cupcake.size)

class Large(Cupcake):
    size = "large"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self. flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

# from abc import ABC

# class Vehicle(ABC):
#     pass

cupcake1 = Cupcake("Stars and Stripes", 2.99, "Vanilla", "Chocolate")
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3
]

def write_new_csv(file, cupcakes):
    with open(file, 'w', newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "sprinkles": cupcake.sprinkles})



def add_cupcake(file, cupcake):
    with open(file, 'a', newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        

        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "sprinkles": cupcake.sprinkles})


write_new_csv("sample.csv", cupcake_list)