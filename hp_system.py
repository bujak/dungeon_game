
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

def restore_char_hp(inventory_weight, inventory_numbers, cloth_armour_class, char_hp):
    food_restore = {'bitten apple' : 0.5, 'cookies': 1, 'beer':2, 'vodka': 3}
    max_health = 1
    for item in inventory_numbers:
        if item in cloth_armour_class:

            max_health += cloth_armour_class[item]

    if char_hp < max_health:

        chosen_food = input("Please indicate which food you would like to eat to restore your health: ")

        if chosen_food in food_restore:
            char_hp += food_restore[chosen_food]
            print("Mmmm tasty! You feel now much better!")
            print("Now you have %d health points!" %char_hp)
            if inventory_numbers[chosen_food] > 1:
                inventory_numbers[chosen_food] -= 1
                inventory_weight[chosen_food] -= (inventory_weight[chosen_food]/2)

            else:
                del inventory_numbers[chosen_food]
                del inventory_weight[chosen_food]
            return char_hp

        elif chosen_food not in food_restore:
            print("Sorry, you don't have such food in your inventory.")

    else:
        print("You are in full health. Maybe don't waste your food now.")
