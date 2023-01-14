class santa_village:
    counter_of_residents = 0
    counter_of_buildings = 0

    def count_resident(self):
        santa_village.counter_of_residents += 1
    def count_buildings(self):

        santa_village.counter_of_buildings += 1

class buildings(santa_village):
    def __init__(self, name):
        self.name = name
        super().count_buildings()

class dweller(santa_village):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().count_resident()

    def introduce_yourself(self):
        print(f"Hi! I'm {self.name} and have {self.age} old.")

class reindeer(dweller):
    def __init__(self, name, age, nose_colour):
        super().__init__(name,age)
        self.nose_colour = nose_colour

    def introduce_yourself(self):
        super().introduce_yourself()
        print(f"And I'm a reindeer and have {self.nose_colour} nose.")

class elf(dweller):

    def introduce_yourself(self):
        super().introduce_yourself()
        print(f"And I'm an Elf.")

    def make_present(self):
        present()

class present:
    number_of_presents = 0
    def __init__(self):
        present.number_of_presents += 1

class letter:
    def __init__(self, requests):
        self.requests = requests

class santa(letter):
    def __init__(self, requests):
        super().__init__(requests)
        self.readed = True


