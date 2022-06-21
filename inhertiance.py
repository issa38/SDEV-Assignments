class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

# Creating Catt class


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Creating walk object

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sunday(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Assigning the Age of the cats as well
simon = Cat('Simon', 2)
sally = Cat('Sally', 3)
sunday = Cat('Sunday', 1)

cats = [simon, sally, sunday]

pets = Pets(cats)


for i in range(len(cats)):
    pet = cats[i]
    print(pet.walk())
