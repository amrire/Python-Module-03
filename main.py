#!/usr/bin/python3
from claptrap import ClapTrap
from scavtrap import ScavTrap


if __name__ == '__main__':
    claptrap = ClapTrap("CT-01")
    claptrap.attack("Enemy-01")
    claptrap.take_damage(5)
    claptrap.be_repaired(3)
    claptrap.attack("Enemy-02")
    claptrap.take_damage(15)
    scavtrap = ScavTrap("ST-01")
    scavtrap.attack("Enemy-01")
    scavtrap.guard_gate()
    scavtrap.take_damage(40)
    scavtrap.be_repaired(20)
    scavtrap.attack("Enemy-02")
    scavtrap.take_damage(100)
