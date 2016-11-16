from gameboard_boxes import *
from inventory import *



def increasing_char_hp(inventory_numbers,cloth_armour_class):
    if inventory_numbers == False:
        hp = 1
        return hp
    else:
        hp = 1
        for item in inventory_numbers:
            if item in cloth_armour_class:

                hp += cloth_armour_class[item]

        return hp

def restore_char_hp(inventory_numbers, cloth_armour_class, food_restore):
    if char_hp < (1 += cloth_armour_class.values()):
        chosen_food = input("Please indicate which food you would like to eat to restore your health: ")
        if chosen_food in food_restore:
            char_hp += food_restore[chosed_food]
            print("Mmmm tasty! You feel now much better!")
            if inventory_numbers[chosen_food] > 1:
                inventory_numbers[chosen_food] -= 1
                inventory_weight[chosen_food] -= (inventory_weight[chosen_food]/2)
            else:
                del inventory_numbers[chosen_food]
                del inventory_weight[chosen_food]
            return char_hp, inventory_numbers, inventory_weight

        else:
            print("Sorry, you don't have such food in your inventory.")

    else:
        print("You are in full health. Maybe don't waste your food now.")
