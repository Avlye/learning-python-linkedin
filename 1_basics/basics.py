name = "Avlye"
age = 23

# Type of #{name}
print("Type of {}".format(name))
print(type(name))

print("Spelling for you: ")

for letter in name:
    print(letter, " ...")


# Conditionals
def is_vote_needed():
    # In a real case,
    # this function shouldn't printout
    # but it's just a exercise ... so, that ok.
    if age >= 18 and age <= 60:
        print("{} needs to vote".format(name))
        return True
    else:
        print("{} doesn't need to vote".format(name))
        return False


class Animal:
    def __init__(self, name, sound=None):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print("{} is making sound of: {}".format(self.name, self.sound))


class Cat(Animal):
    # overrides Animal.make_sound
    def make_sound(self):
        print("Miau!!!")

    def show_info(self):
        print(self.name, "is a awesome cat because is part of ",
              self.__class__)


cat = Cat(name)
cat.make_sound()
cat.show_info()