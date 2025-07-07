class DinoDev:
    def __init__(self, name, age, passion):
        self.name = name
        self.age = age
        self.passion = passion
    
    def roar(self):
        print(f"{self.name} roars: 'I love {self.passion} and building cool stuff!'")

me = DinoDev("Maip Macrothorax", 20, "Data Science")
me.roar()
