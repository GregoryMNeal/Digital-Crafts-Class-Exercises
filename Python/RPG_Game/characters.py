# Base Character Class
class Character:

    def __init__ (self, name):
        self.name = name

    @classmethod
    def get_classname(cls):
        return cls.__name__

    def alive (self):
        if self.health > 0:
            return True
        else:
            return False

    def attack (self, other_guy):
        other_guy.health -= self.power
        if other_guy.get_classname() == Hero:
            print("You do {} damage to the goblin.".format(self.power))
        else:
            print("The goblin does {} damage to you.".format(self.power))

# Goblin Class
class Goblin (Character):

    def __init__ (self, name):
        super().__init__(name)
        self.health = 6
        self.power = 2

    def print_status (self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))

# Hero Class
class Hero (Character):

    def __init__ (self, name):
        super().__init__(name)
        self.health = 10
        self.power = 5

    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

# Medic Class
class Medic (Character):

    def __init__ (self, name):
        super().__init__(name)

    def heal(self, patient):
        patient.health += 2

# Shadow Class
class Shadow (Character):

    def __init__ (self, name):
        super().__init__(name)
        self.health = 1
        self.times_attacked = 0

# Zombie Class - doesn't die
class Zombie (Character):

    def __init__ (self, name):
        super().__init__(name)

# Haiki Class - she shoots a graduated response laser out of her eyes.
#  She can vary the power of the laser depending on the application anywhere
#  from 5 watts (enough to start a campfire) to 100,000 watts (military grade).
#  The higher the watts the greater the damage she can do.

class Haiki (Character):

    def __init__ (self, name, watts):
        super().__init__(name)
