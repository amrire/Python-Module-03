#!/usr/bin/python3
from claptrap import ClapTrap
from scavtrap import ScavTrap
from fragtrap import FragTrap


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
    fragtrap = FragTrap("FT-01")
    fragtrap.attack("Enemy-01")
    fragtrap.high_fives_guys()
    fragtrap.take_damage(50)
    fragtrap.be_repaired(30)
    fragtrap.attack("Enemy-02")
    fragtrap.take_damage(150)
