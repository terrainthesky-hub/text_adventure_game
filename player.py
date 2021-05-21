# Write a class to hold player information, e.g. what room they are in
# currently.
import random
class Player:
    def __init__(self, location, hp=200, xp=0, level=0, attack=0, heal=0):
        self.location = location
        self.inventory = []
        self.hp = hp
        self.attack = attack
        self.heal = heal
        self.equipment = []
        self.xp = xp
        self.level = level

    def __str__(self):
        return (f'Your location is {self.location}. Your inventory is {self.inventory}')
    def add_to_inventory(self, item):
        self.inventory.append(item)
        self.print_inventory()

    def remove_from_inventory(self, item):
        self.inventory.remove(item)
        self.print_inventory()
    def equip_item(self, item):
        self.equipment.append(item)
        self.print_equipment()
    def unequip_item(self, item):
        self.equipment.remove(item)
        self.print_equipment()

    def print_inventory(self):
        print("Your inventory is", [f"{c} : {p.name}: {p.description}" for c, p in enumerate(self.inventory)])

    def print_equipment(self):
         print("Your equipment is", [f"{c} : {p.name}: {p.description}" for c, p in enumerate(self.equipment)])

 
   
    # def dict_from_class(cls):
    #     return dict((key, value) for (key, value) in cls.__dict__.items()
    #     if key not in _excluded_keys)
