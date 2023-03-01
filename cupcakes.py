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

from abc import ABC, abstractmethod

class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor,frosting, filling):
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

# from abc import ABC

# class Vehicle(ABC):
#     pass