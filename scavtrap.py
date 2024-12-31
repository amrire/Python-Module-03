#!/usr/bin/python3
from claptrap import ClapTrap


class ScavTrap(ClapTrap):
    def __init__(self, name):
        super().__init__(name)
        self.hit_points = 100
        self.energy_points = 50
        self.attack_damage = 20
        print(f"ScavTrap {self.name} has been created with enhanced attributes!")
        
    def attack(self, target):
        if self.energy_points > 0 and self.hit_points > 0:
            print(f"ScavTrap {self.name} ferociously attacks {target}, causing {self.attack_damage} points of damage!")
            self.energy_points -= 1
        else:
            print(f"ScavTrap {self.name} cannot attack! Not enough energy or hit points.")
            
    def guard_gate(self):
        print(f"ScavTrap {self.name} is now in Gatekeeper mode! Protecting the gate with full focus.")

    def __del__(self):
        print(f"ScavTrap {self.name} has been destroyed!")
