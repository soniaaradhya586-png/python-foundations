import random


class Hat:

    #def __init__(self):
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        #house = random.choices(self.houses)
        #print(name, "is in", "some house")
        print(name, "is in", random.choice(cls.houses))


#hat = Hat()
Hat.sort("Harry")