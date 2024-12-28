# Python Module 03: Mastering OOP Concepts - Inheritance and Polymorphism

Welcome to **Module 03**, where we dive deep into object-oriented programming (OOP) concepts using Python. This module focuses on inheritance and polymorphism, two fundamental principles of OOP, through a series of hands-on exercises. By completing these exercises, you'll strengthen your understanding of class hierarchies, method overriding, and multiple inheritance.

---

## **Contents**

1. [Introduction](#introduction)
2. [Exercises](#exercises)
   - [Exercise 00: Aaaaand... OPEN!](#exercise-00-aaaaand-open)
   - [Exercise 01: Serena, my love!](#exercise-01-serena-my-love)
   - [Exercise 02: Repetitive work](#exercise-02-repetitive-work)
   - [Exercise 03: Now it’s weird!](#exercise-03-now-its-weird)
3. [General Rules](#general-rules)
4. [Resources](#resources)

---

## **Introduction**

In this module, you will build a series of interconnected classes using Python, starting with a simple base class and gradually expanding its functionality through inheritance. Each exercise introduces a new layer of complexity, culminating in a class that demonstrates multiple inheritance. This approach will solidify your understanding of OOP principles while also challenging your problem-solving skills.

---

## **Exercises**

### **Exercise 00: Aaaaand... OPEN!**

- **Objective**: Implement a base class `ClapTrap` with attributes like `name`, `hit_points`, `energy_points`, and `attack_damage`.
- **Key Features**:
  - Actions: `attack`, `take_damage`, `be_repaired`
  - Print descriptive messages for each action.

**Files to turn in**:
- `claptrap.py`
- `main.py`

---

### **Exercise 01: Serena, my love!**

- **Objective**: Create a derived class `ScavTrap` that inherits from `ClapTrap`.
- **Key Features**:
  - Override specific attributes and methods.
  - Add a new method `guard_gate`.

**Files to turn in**:
- `claptrap.py`
- `scavtrap.py`
- `main.py`

---

### **Exercise 02: Repetitive work**

- **Objective**: Create another derived class `FragTrap` that extends `ClapTrap`.
- **Key Features**:
  - Override specific attributes and methods.
  - Add a new method `high_fives_guys`.

**Files to turn in**:
- `claptrap.py`
- `fragtrap.py`
- `main.py`

---

### **Exercise 03: Now it’s weird!**

- **Objective**: Create a hybrid class `DiamondTrap` that inherits from both `ScavTrap` and `FragTrap`.
- **Key Features**:
  - Handle attribute and method conflicts.
  - Add a new method `who_am_i`.

**Files to turn in**:
- `claptrap.py`
- `scavtrap.py`
- `fragtrap.py`
- `diamondtrap.py`
- `main.py`

---

## **General Rules**

- Ensure your code is clean, readable, and modular.
- Test all functionality in a separate `main.py` file.
- Follow Python naming conventions and best practices.
- Avoid hardcoding values where possible.
- Handle invalid states (e.g., zero energy points).

---

## **Resources**

- [Python Classes](https://docs.python.org/3/tutorial/classes.html)
- [Inheritance in Python](https://realpython.com/inheritance-composition-python/)
- [Method Resolution Order (MRO)](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Encapsulation and Polymorphism](https://realpython.com/python3-object-oriented-programming/)

---

## **How to Run**

1. Clone the repository or download the project files.
2. Ensure you have Python 3.x installed on your system.
3. Navigate to the directory containing the exercises.
4. Run `main.py` to test the functionality of each exercise.

---

## **Conclusion**

By completing Module 03, you will gain practical experience with Python OOP principles, setting a strong foundation for more advanced topics like abstract classes, interfaces, and design patterns. Happy coding!
