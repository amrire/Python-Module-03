#!/usr/bin/python3
from claptrap import ClapTrap


class FragTrap(ClapTrap):
    def __init__(self, name):
        super().__init__(name)
        self.hit_points = 100
        self.energy_points = 100
        self.attack_damage = 30
        print(f"FragTrap {self.name} has been created with enhanced attributes!")
        
    def attack(self, target):
        if self.energy_points > 0 and self.hit_points > 0:
            print(f"FragTrap {self.name} powerfully attacks {target}, causing {self.attack_damage} points of damage!")
            self.energy_points -= 1
        else:
            print(f"FragTrap {self.name} cannot attack! Not enough energy or hit points.")
            
    def high_fives_guys(self):
        print(f"FragTrap {self.name} requests a positive high five! Anyone? High fives all around!")

    def __del__(self):
        print(f"FragTrap {self.name} has been destroyed!")
		