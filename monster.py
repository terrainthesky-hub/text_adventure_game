import random

class Monsters:
    def __init__(self, name, visual, xp=0, hp=None, attack=None):
        self.name = name
        self.visual = visual
        self.hp = hp
        self.attack = attack
        self.xp = xp




    def __str__(self):
        return f"{self.name}: {self.visual}"
