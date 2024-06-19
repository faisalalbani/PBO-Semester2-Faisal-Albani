from abc import ABC, abstractmethod
import random
class Hero(ABC):
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp
    @abstractmethod
    def active_skill(self):
        pass
    @abstractmethod
    def passive_skill(self):
        pass
    @abstractmethod
    def ulti(self):
        pass
class Marksman(Hero):
    def active_skill(self,enemy):
        critical = self.passive_skill()
        damage = int(self.attack*critical)
        enemy.hp -= damage
        print(f"{self.name} deals damage {damage} to {enemy.name}")
        print(f"{enemy.name} HP remains {enemy.hp}")

    def passive_skill(self):
        return 1.0 + random.random()
    def ulti(self):
            pass

class Tank(Hero):
    def active_skill(self,enemy):
        heal = int(self.passive_skill()*self.hp)
        self.hp += heal
        enemy.hp -= self.attack
        print(f"{self.name} heals {heal}, current HP {self.hp}")
        print(f"{self.name} deals damage {self.attack} to {enemy.name}")
        print(f"{enemy.name} HP remains {enemy.hp}")

    def passive_skill(self):
        return random.random()*0.3
    def ulti(self):
        pass
    
balmond = Tank("Balmond", 100, 2500)
layla = Marksman("Layla", 210, 1600)
print("=== Turn 1 ===")
layla.active_skill(balmond)
print("=== Turn 2 ===")
balmond.active_skill(layla)

#----------------------------------

from abc import ABC, abstractmethod
from math import pi

class Shape (ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @abstractmethod
    def area (self):
        pass

    @abstractmethod
    def perimeter (self):
        pass

class Rectangle (Shape):
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle (Shape): 
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius **2
    
    def perimeter(self):
        return 2 * pi * self.radius
    
persegipanjang = Rectangle (3, 4)
bulat = Circle (8)

print (persegipanjang.area())
print (persegipanjang.perimeter())

print (bulat.area())
print (bulat.perimeter())