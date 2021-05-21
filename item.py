import random

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

class Health_Potion(Item):
    def __init__(self, name='', description='', heal=0, **kwargs):
        super().__init__(name, description, **kwargs)
        self.name = name
        self.description = description
        self.heal = heal

    def __str__(self):
        return f"{self.name}: {self.description}"

class Weapon(Item):
    def __init__(self, damage=0, **kwargs):
        super().__init__(**kwargs)
        self.damage = damage

    def __str__(self):
        return f"{self.name}: {self.description}"

    