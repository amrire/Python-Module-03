#!/usr/bin/python3
from claptrap import ClapTrap

if __name__ == '__main__':
    claptrap = ClapTrap("CT-01")
    claptrap.attack("Enemy-01")
    claptrap.take_damage(5)
    claptrap.be_repaired(3)
    claptrap.attack("Enemy-02")
    claptrap.take_damage(15)
