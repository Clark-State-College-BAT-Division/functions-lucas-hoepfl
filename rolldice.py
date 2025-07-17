#Write a function that takes as input number of dice and number of sides. The function will then return a list
#of randomly generated numbers in the proper count and range. For example if the function is asked to generate
#3D6 or three six sided dice, then a potential output would be [2,2,6]
#This function cannot have any input or print statements.
#Write supporting code that will ask the user for number of dice and sides, call the function, then report the results.
#The function should not be called if number of dice is zero or less and instead should report bad input to the user
#The function should not be called if number of sides is 1 or less and instead should report bad input to the user
#Sample outputs (your text does not have to match exactly)

# How many dice to roll? 3
# How many sides? 6
# Here are the results: [6, 1, 6]

# How many dice to roll? 0
# How many sides? 5
# Error: Sides must be greater than 1 and dice count greater than 0.

# How many dice to roll? 20
# How many sides? 20
# Here are the results: [18, 19, 6, 8, 13, 6, 6, 6, 18, 12, 20, 10, 14, 8, 14, 17, 12, 15, 20, 17]

import random

def dice_roll(dice_quantity, dice_num_sides):
    all_rolls = []
    for _ in range(dice_quantity):
        single_roll = random.randint(1, dice_num_sides)
        all_rolls.append(single_roll)
    return all_rolls

def main_function():
    while True:
        dice_quantity = int(input("How many dice are you rolling? "))
        dice_num_sides = int(input("How many sides do your dice have? "))
        if dice_num_sides >= 1 and dice_quantity >= 0:
            break
        else:
            print("Dice must have more than 1 side and you must roll at least 1 die.")
    all_rolls = dice_roll(dice_quantity, dice_num_sides)
    print("You rolled: ", all_rolls)


if __name__ == "__main__":
    main_function()