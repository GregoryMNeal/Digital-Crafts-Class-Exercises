# Base Character Class
class Character:

    def __init__ (self, name):
        self.name = name

    def probability (self, events, outcomes):
        result = (events / outcomes) * 100
        return result

    def alive (self):
        if self.health > 0:
            return True
        else:
            return False

    def attack (self, other_guy):
        other_guy.health -= self.power
        if self.name == 'Greg':
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

# Zombie Class - doesn't die
class Zombie (Character):

    def __init__ (self, name):
        super().__init__(name)

# Haiki Class - she shoots various types of lasers from her eyes
#   based on the application
class Haiki (Character):
