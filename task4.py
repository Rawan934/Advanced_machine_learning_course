from abc import ABCMeta,abstractmethod
class animal(metaclass=ABCMeta):
    @abstractmethod
    def sound_animal(self):
        pass
    def describe(self):
        print(" an animal ")
class dog(animal):
    def sound_animal(self):
        return "haw haw"
class descripe (animal):
    print("dogs are one of the most lovely and frindely pets ")
class cat(animal):
    def sound_animal(self):
        return"meow"
class descripe(animal):
    print("cats are very cute")
class cow (animal):
    def sound_animal(self):
        return  "moo"
class descripe(animal):
    print("cows are big ")

    animals = [dog(), cat().cow()]

for animal in animal:
    print(f"{animal.__class__.__name__}:")
    print("Sound:", animal.sound_animal())
    animal.describe()
    print()
    