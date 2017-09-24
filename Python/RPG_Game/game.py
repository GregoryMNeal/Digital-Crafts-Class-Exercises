#!/usr/bin/env python
from characters import Hero, Goblin
# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

def main():
    good_guy = Hero('Greg')
    bad_guy = Goblin('Godzilla')
    zombie_guy = Zombie('Spicoli')

    while bad_guy.alive() and good_guy.alive():
        good_guy.print_status()
        bad_guy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            good_guy.attack(bad_guy)
            if bad_guy.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if bad_guy.health > 0:
            # Goblin attacks hero
            bad_guy.attack(good_guy)
            if good_guy.health <= 0:
                print("You are dead.")

main()
