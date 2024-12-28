#!/usr/bin/python3


class ClapTrap:
    def __init__(self, name):
        self.name = name
        self.hit_points = 10
        self.energy_points = 10
        self.attack_damage = 10
        print(f"ClapTrap {self.name} has been created!")
        
    def attack(self, target):
        if self.energy_points > 0 and self.hit_points > 0:
            print(f"ClapTrap {self.name} attacks {target}, causing {self.attack_damage} points of damage!")
            self.energy_points -= 1
        else:
            print(f"ClapTrap {self.name} cannot attack! Not enough energy or hit points.")

    def take_damage(self, amount):
        self.hit_points -= amount
        if self.hit_points < 0:
            self.hit_points = 0
        print(f"ClapTrap {self.name} takes {amount} points of damage! Remaining hit points: {self.hit_points}")
    
    def be_repaired(self, amount):
        if self.energy_points > 0 and self.hit_points > 0:
            self.hit_points += amount
            self.energy_points -= 1
            print(f"ClapTrap {self.name} is repaired by {amount} hit points! Remaining hit points: {self.hit_points}")
        else:
            print(f"ClapTrap {self.name} cannot be repaired! Not enough energy or hit points.")
            
    def __del__(self):
        print(f"ClapTrap {self.name} has been destroyed!")
