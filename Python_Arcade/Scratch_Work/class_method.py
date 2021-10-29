# Review Questions

'''1. Create a class called Cat. Give it attributes for name, color, and weight.
Give it a method called meow.
Create an instance of the cat class, set the attributes, and call the meow method.'''
class Cat:


    def __init__(self):

        self.name = ""
        self.color = ""
        self.weight = ""

    def meow(self):
        print("Meow")

def main():

    Maddie = Cat()
    Maddie.name = "Maddie"
    Maddie.color = "White"
    Maddie.weight = 10
    Maddie.meow()

main()

"""2. Create a class called Monster. Give it an attribute for name and an integer attribute 
for health. Create a method called decrease_health that takes in a parameter 
amount and decreases the health by that much.
Inside that method, print that the animal died if health goes below zero."""

class Monster():
    name = ""
    health = 5

def decrease_health(health):
    Monster.health += -1
    if Monster.health <= 0:
        print("Your monster has died. :(")


def main():
    uga_buga = Monster()
    uga_buga.name = "Uga Buga"

    decrease_health(uga_buga)
    print(uga_buga.health)


main()