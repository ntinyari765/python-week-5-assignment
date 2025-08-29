# Creating a class to represent a flower
# Parent class
class Flower:
    def __init__(self, name, color, season):
        self.name = name
        self.color = color
        self.season = season

    def bloom(self):
        return f"The {self.name} blooms in {self.season} with beautiful {self.color} flowers."
    
    def fragrance(self):
        return f"The {self.name} has a delightful fragrance."
    
# Child class inheriting from Flower
class Rose(Flower):
    def __init__(self, color, season, thorns=True):
        super().__init__("Rose", color, season)
        self.thorns = thorns
    
    # Overriding method (Polymorphism)
    def fragrance(self):
        print(f"The {self.color} Rose smells sweet and romantic")

class Daisy(Flower):
    def __init__(self, color, season):
        super().__init__("Daisy", color, season)
    
    def fragrance(self):
        print(f"The {self.color} Daisy has a light, fresh scent")

# Creating objects
f1 = Flower("Peony", "Pink", "Spring")
f2 = Rose("Red", "Summer")
f3 = Daisy("White", "Spring")

# Using methods
f1.bloom()
f1.fragrance()

f2.bloom()
f2.fragrance()

f3.bloom()
f3.fragrance()

    
