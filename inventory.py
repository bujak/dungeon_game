import  random

from hp_system import *


weapons_damage = {'rainbow sword of sir Charlie the Unicode': 3, 'dwarven axe from Lambda': 4, 'bow from Ascii': 2,
               'warhammer of 40 000 lost souls': 5}
cloth_armour_class = {'chromium chainmail' : 4, 'boots of Master Java' : 2, 'Elif gloves': 1, 'belt of Loop': 1}



clothes = {'chromium chainmail' : 4, 'boots of Master Java': 2, 'Elif gloves': 1, 'belt of Loop':1 }
food = {'bitten apple' : 0.5, 'cookies': 0.5, 'beer' : 1, 'vodka' : 1}

weapons = {'rainbow sword of sir Charlie the Unicode' : 2, 'dwarven axe from Lambda': 2, 'bow from Ascii': 1, 'warhammer of 40 000 lost souls' : 3}

other = {'gemstone from Git continent' : 1, 'ruby' : 1,'gold coins' : 0.5, 'mysterious code' : 0.5}

def generating_loot():
    '''Function that generates loot'''

    loot_gen = (clothes,food,weapons,other) #chooses randomly type of content
    type_of_loot = loot_gen[random.randrange(0,3)] #chooses randomly item (key)
    generating_item = random.sample(list(type_of_loot), 1)
    loot_item = ''.join(generating_item)
    loot = {loot_item: type_of_loot[loot_item]} #generates dict with randomly choosen item (item:weight)

    return loot


def positioning_loot(gameboard):
    '''Positioning triggers for loot on gameboard'''

    tries = 0

    while tries != 8:
        loot_position_column = random.randrange(1,88)
        loot_position_row = random.randrange(1,27)

        if gameboard[loot_position_row][loot_position_column] != "#":
            gameboard[loot_position_row][loot_position_column] = "L"
            tries += 1

    return gameboard


def adding_loot(inventory_weight, inventory_numbers):
    '''Collecting loot.'''
    looting = generating_loot()
    item = ''.join(looting.keys())

    if len(inventory_weight.keys()) == 0:
        inventory_weight.update(looting)
    else:
        if sum(inventory_weight.values()) > 12:
            print("Your inventory is too heavy! You can't take anything more.")

        else:
            if item in inventory_weight:

                inventory_weight[item] += looting[item]
            else:
                inventory_weight.update(looting)

    if len(inventory_numbers.keys()) == 0:
        inventory_numbers[item] = 1
    else:
        if sum(inventory_weight.values()) > 12:
            print("\n")

        else:
            if item in inventory_numbers:
                inventory_numbers[item] += 1
            else:
                inventory_numbers[item] = 1

    increasing_char_hp(inventory_numbers,cloth_armour_class)
    print('\n' * 30)
    print("Yay! You have found %s!" %item)  #print_acquired item
    return inventory_weight, inventory_numbers


def dropping_item(inventory_weight, inventory_numbers):
    '''Dropping unnecessary items from inventory.'''

    print_inventory(inventory_weight, inventory_numbers)

    item_to_remove = input("\nPlease indicate the name of the item you would like to remove from your inventory: ")


    if item_to_remove in inventory_numbers:
        if inventory_numbers[item_to_remove] > 1:
            inventory_numbers[item_to_remove] -= 1
            inventory_weight[item_to_remove] -= (inventory_weight[item_to_remove]/2)

        else:
            del inventory_numbers[item_to_remove]
            del inventory_weight[item_to_remove]

    else:
        print("You don't have such item.")

    return inventory_weight, inventory_numbers


def print_inventory(inventory_weight, inventory_numbers):
    '''Function that displays inventory in a specific order or without any
    order.The order input argument can be as follow: empty (by default) which
    means that the inventory is unordered;
    "count.desc" means the inventory is ordered in descending order;
    "count,asc" means the inventory is ordered in ascending order.
    '''

    clothes = ('clothes', 'chromium chainmail', 'boots of Master Java', 'Elif gloves', 'belt of Loop')
    food = ('food', 'bitten apple', 'cookies', 'beer', 'vodka')

    weapons = ('weapons', 'rainbow sword of sir Charlie the Unicode', 'dwarven axe from Lambda', 'bow from Ascii',
                   'warhammer of 40 000 lost souls')

    other = ('other', 'gemstone from Git continent', 'ruby','gold coin' , 'mysterious code')
    len_keys = []

    for key in inventory_weight.keys():
        len_keys.append(len(key))

    max_len_item_name = (max(len_keys))  #calculates the maximum length of key
    max_len_weight = len(str(max(inventory_weight.values())))  #calculactes max length
                                                        #of value

    sorted_values = sorted(inventory_numbers.values())


    print('\n'*30)
    print('\nInventory:\n')

    column_item_num = 5
    column_item_type = 9
    column_item_name = (max_len_item_name + column_item_num + column_item_type + 4)
    column_weight = int(column_item_name + column_item_num + column_item_type + 1)
    item_types = (clothes,food,weapons,other)

    all_columns = column_item_num + column_item_type + column_item_name + column_weight

    print("{0:>{1}}".format("count", column_item_num)
          + "{0:>{1}}".format("type", column_item_type) + "{0:>{1}}".format("name", column_item_name)
          + "{0:>{1}}".format("weight",column_weight))

    print("{0:>{1}}".format("-" * all_columns, all_columns))

    total = 0

    for item in sorted(inventory_numbers, key = inventory_numbers.get, reverse = True):
        total += int(inventory_numbers.get(item))
        loot_type = ""

        for it_type in range(len(item_types)):
            if item in item_types[it_type]:
                loot_type += item_types[it_type][0]

        print('{0:>{1}}'.format(str(inventory_numbers.get(item)), column_item_num)
                  + '{0:>{1}}'.format(loot_type, column_item_type) + '{0:>{1}}'.format(item, column_item_name)
                  + '{0:>{1}}'.format(str(inventory_weight.get(item)), column_weight))
