# Implement a class to hold room information. This should have name and
# description attributes.
class Rooms:
    def __init__(self, name, description, item=[]):
        self.name = name
        self.description = description
        self.item = item
        self.inventory = []

    def __str__(self):
        return f"{self.name}: {self.description}"

    def add_to_inventory_room(self, item):
        self.inventory.append(item)

    def remove_from_inventory_room(self, item):
        self.inventory.remove(item)

    def print_room_inventory(self):
        print("The rooms inventory is", [f"{c} : {p.name}: {p.description}" for c, p in enumerate(self.inventory)])

 
 