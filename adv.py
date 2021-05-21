from monster import Monsters
from room import Rooms
from player import Player
from item import Item
from item import Weapon
from item import Health_Potion
import random

# Declares all the rooms and items

room = {
    'outside':  Rooms("Outside Cave Entrance",
                     "North of you, the cave mount beckons",  [Item("HealthPotion", "Refills health")]),

    'foyer':    Rooms("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("HealthPotion", "Refills health")]),

    'overlook': Rooms("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("ShortSword", "dull rusty blade")]),

    'narrow':   Rooms("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("BrokenShield", "broken but still usable")]),

    'treasure': Rooms("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("GoldCoin", "remnants of what was once left here")]),
}

# Decaleres the enemies

monster = {
    'lycan': Monsters("Lycan", """
                                                  ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L|
                \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `|
                -,-..\  _  \  `  /  ,  / `._) _,-\`       |
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               |
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`"""), 
 'dino': Monsters("dino", """
    oo`'._..---.___..-
 (_,-.        ,..'`
      `'.    ;
         : :`
        _;_; """),

    'pikachu': Monsters("pikachu", """

       ,___          .-;'
       `"-.`\_...._/`.`
    ,      \        /
 .-' ',    / ()   ()\\ 
`'._   \  /()    .  (|\\
    > .' ;,     -'-  / 
   / <   |;,     __.;
   '-.'-.|  , \    , \\ 
      `>.|;, \_)    \_)
       `-;     ,    /
          \    /   <
           '. <`'-,_)
            '._""")
    }

# Links rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# roominv = Player(room['outside'])

# outside_room = Player(room['outside'])


healthpot = Health_Potion(name="HealthPotion", description="Heals for 30-40 hp", heal=random.randint(1,10) + 30)
greaterhealthpot = Health_Potion(name="Greater HealthPotion", description="Heals for 80-100 hp", heal=random.randint(10,20) + 80)
barehands = Weapon(name="Bare Hands", description='Just your fists', damage=random.randint(1,5) + 15)
sword = Weapon(name="ShortSword", description="dull rusty blade", damage=random.randint(5,10) + 20)


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

outside = room['outside']
outside.add_to_inventory_room(healthpot)
foyer = room['foyer']
foyer.add_to_inventory_room(greaterhealthpot)
overlook = room['overlook']
overlook.add_to_inventory_room(sword)
narrow = room['narrow']
narrow.add_to_inventory_room(room['narrow'].item[0])
treasure = room['treasure']
treasure.add_to_inventory_room(room['treasure'].item[0])



def prompt(message):
    print(f">> {message}")


def location_info():
    prompt(f"You are in the {player.location}\n")
    prompt(f"Found items: {player.location.print_room_inventory()}\n")


def direction_error(direction):
    if direction == "n":
        prompt("No way North!\n")
    elif direction == "e":
        prompt("No way East!\n")
    elif direction == "s":
        prompt("No way South!\n")
    elif direction == "w":
        prompt("No way West!\n")

def level_up():
    if player.xp == 0 and player.level == 1:
        player.level = 1
        player.xp = 0
    if player.xp >= 150 and player.level == 1:
        player.level = 2
        player.hp += 25
        print("You've leveled up to level 2!")
    if player.xp >= 300 and player.level == 2:
        player.level = 3
        player.hp += 25
        print("You've leveled up to level 3!")
    if player.xp >= 500 and player.level == 3:
        player.level = 4
        player.hp += 25
        print("You've leveled up to level 4! You're max level!")

def enemies(local):
    fight_list = ['fight', 'freedom1', 'freedom2', 'freedom3']
    fight = random.choice(fight_list)

    lycan = monster['lycan']
    dino = monster['dino']
    pikachu = monster['pikachu']

    enemy_list = [lycan, dino, pikachu]
    enemy = random.choice(enemy_list)

    if enemy == lycan:
        enemy.hp = 150
        enemy.xp = 100
    elif enemy == dino:
        enemy.hp = 100
        enemy.xp = 50
    elif enemy == pikachu:
        enemy.hp = 200
        enemy.xp = 150




    if fight == 'fight':
        print(f"You've encountered a {enemy.name}!")
        print(enemy.visual)
        while enemy.hp > 0:
            attack_input = input("a for attack or l for Heal: ")
            if attack_input == "a":
                if enemy == lycan:
                    enemy.attack = random.randint(1,5) + 10
                elif enemy == dino:
                    enemy.attack = random.randint(1,3) + 5
                elif enemy == pikachu:
                    enemy.attack = random.randint(1,10) + 10
                
                if sword in player.equipment:
                    print("You have a shortsword!")
                    if player.level == 1:
                        player.attack = random.randint(1,10) + 25
                    if player.level == 2:
                        player.attack = player.attack = random.randint(1,10) + 30
                    if player.level == 3:
                        player.attack = player.attack = random.randint(1,10) + 35
                    if player.level == 4:
                        player.attack = player.attack = random.randint(1,10) + 40
                else:
                    print("You're using your fists!")
                    if player.level == 1:
                        player.attack = player.attack = random.randint(1,10) + 20
                    if player.level == 2:
                        player.attack = player.attack = random.randint(1,10) + 25
                    if player.level == 3:
                        player.attack = player.attack = random.randint(1,10) + 30
                    if player.level == 4:
                        player.attack = player.attack = random.randint(1,10) + 35
                
                enemy.hp -= player.attack
                player.hp -= enemy.attack
                print(f"You attacked for {player.attack}")
                print(f"You've been attacked for {enemy.attack} you have {player.hp} health left")
                print(f"The {enemy.name} has {enemy.hp} health")
            if attack_input == "l":
                    player.print_inventory()
                    if healthpot in player.inventory:
                        player.heal += healthpot.heal
                        player.remove_from_inventory(healthpot)
                        player.hp -= enemy.attack
                        player.hp += player.heal
                        print(f"The {enemy.name} attacked you for {enemy.attack}")
                        print(f"You've healed for {player.heal} you now have {player.hp} health")
                        print(f"The {enemy.name} has {enemy.hp} health")
                    elif greaterhealthpot in player.inventory:
                        player.heal += greaterhealthpot.heal
                        player.remove_from_inventory(greaterhealthpot)
                        player.hp -= enemy.attack
                        player.hp += player.heal
                        print(f"The {enemy.name} attacked you for {enemy.attack}")
                        print(f"You've healed for {player.heal} you now have {player.hp} health")
                        print(f"The {enemy.name} has {enemy.hp} health")
                    else:
                        print("You have no healing potions")
            if enemy.hp <= 0:
                print(f"You've defeated a {enemy.name}!")
                player.xp += enemy.xp
                level_up()
            if player.hp <= 0:
                break
    else:
        print("You see no enemies in here.\n")


def equip():
    if sword in player.inventory:
        player.equip_item(sword)
        player.remove_from_inventory(sword)
    elif player.inventory == []:
        print("Your inventory is empty, try leaving an picking up a weapon or exiting the room to find one.\n")

def unequip():
    if sword in player.equipment:
        player.add_to_inventory(sword)
        player.unequip_item(sword)
    else:
        print("You have no weapons to unequip.\n")


def stats():
    print(f"""Your stats are: 
    Player level {player.level}
    Hit points: {player.hp}
    Attack damage: {player.attack}
    Player experience points: {player.xp}""")

def pick_up_item(local):
    #checks if the inventory of the room is empty
    if local.inventory == []:
        print("The room is empty, try leaving an item or exiting the room.\n")
    #checks where the player is located
    elif player.location == local:
        
        ##got it to print out inventory and select items based on the one you picked fron an enumarated list
        selected_inventory = local
        player.print_inventory()
        local.print_room_inventory()
        
        try:
            item_selection = input("choose the number of the item to pick up: ")
            item_selection = int(item_selection)
            player.add_to_inventory(selected_inventory.inventory[item_selection])
            local.remove_from_inventory_room(selected_inventory.inventory[item_selection])
           
        except IndexError:
            
            item_selection = input("Choose a valid number in range that is an integer. Choose the number of the item to pick up: ")
            item_selection = int(item_selection)
            player.add_to_inventory(selected_inventory.inventory[item_selection])
            local.remove_from_inventory_room(selected_inventory.inventory[item_selection])

        except:
            print("Non-numeric selection. Please choose a number: ")


def drop_item(local):
    if player.inventory == [] and player.location == local:
        print("Your inventory is empty, try picking up an item.\n")
    elif player.location == local:                
        try:
            player.print_inventory()
            item_selection = input("choose the number of the item to put down: ")
            item_selection = int(item_selection)
            local.add_to_inventory_room(player.inventory[item_selection])
            local.print_room_inventory()
            player.remove_from_inventory(player.inventory[item_selection])
        except IndexError:
            player.print_inventory()
            item_selection = input("Choose a valid number in range that is an integer. Choose the number of the item to put down: ")
            item_selection = int(item_selection)
            local.add_to_inventory_room(player.inventory[item_selection])
            local.print_room_inventory()
            player.remove_from_inventory(player.inventory[item_selection])
        except:
            print("Non-numeric selection. Please choose a number: ")

def print_commands():
    prompt(
        f"""Commands:
        n - go to North
        e - go to East
        s - go to South
        w - go to West
        i - inventory and equipment
        a - attack
        t - stats
        q - to quit game

        The goal is to get the treasure out of the dungeon!
        """
    )


def try_direction(direction, current_room):
    room_choice = direction + "_to"

    # See if the inputted direction is one we can move to
    if hasattr(current_room, room_choice):
        # fetch the new room
        return getattr(current_room, room_choice)
    else:
        direction_error(direction)
        return current_room

# Make a new player object that is currently in the 'outside' room.
player_name = input("Enter player name: ")
player = Player(room['outside'], level=1, xp=0, attack=0, heal=0)
# player.current_room => room["outside"]

prompt(f"Welcome {player_name}, you are now in the {player.location}")
prompt(player.location.print_room_inventory())
prompt('Type "help" for commands.\n')



while True:
    level_up()
    if room['treasure'].item[0] in player.inventory and player.location == room['outside']:
        prompt("You successfully got the treasure out of the dungeon. Congratulations!")
        break
    if player.hp <= 0:
        print("You were defeated. Better luck next time.\n")
        break
    command = input(f"What do you want to do, {player_name}? ").lower().split()

    if len(command) == 1:
        command = command[0]
        print("command", command)


        # Make player move NSEW
        if command in ["n", "s", "e", "w"]:
            player.location = try_direction(command, player.location)
            location_info()
            enemies(player.location)
            continue
        if command == "help":
            print_commands()
        elif command == "q":
            break
        elif command == "t":
            stats()
        elif command == 'i':
            item_selection = input("grab or leave an item, press 1 to grab an item or 2 to leave one, 3 to equip, 4 to unequip:\n")
            try:
                item_selection = int(item_selection)
            
            except IndexError:
                print("Enter in an integer within range please. \n")
                item_selection = input("grab or leave an item, press 1 to grab an item or 2 to leave one, 3t to equip, 4 to unequip:\n")
                item_selection = int(item_selection)

            if item_selection == 1:
                pick_up_item(player.location)


            elif item_selection == 2:
                drop_item(player.location)

            elif item_selection == 3:
                equip()

            
            elif item_selection == 4:
                unequip()
  

        else:
            prompt("I don't quite understand\n")
    elif len(command) == 2:
        print(command)
    else:
        prompt("I don't quite understand\n")


prompt("Thank you for playing!\n") 

 