class Cupcake:
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
        # self.sprinkles = sprinkles
    
    # def my_method(self):
    #     pass
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)


my_cupcake = Cupcake("Chocolate with fudge filling", 3.99, "Chocolate", "Dark Chocolate", "Fudge")

my_cupcake.add_sprinkles('chocolate', 'blueberry', 'colored sugar')

print(my_cupcake.sprinkles)

# ADDING THINGS TO A CUPCAKE
# my_cupcake.frosting = "Vanilla"
# my_cupcake.filling = "Red Velvet"
# my_cupcake.name = "Valentine's Cupcake"
# my_cupcake.is_miniature = True
# print(my_cupcake.is_miniature)

