import random

def roll_dice(sides=6):
    return random.randint(1, sides)

print("🎲 Welcome to the Dice Roller Simulator!")

while True:
    user_input = input("\nRoll the dice? (yes/no): ").lower()
    if user_input == "yes":
        dice = roll_dice()
        print("You rolled a:", dice)
    elif user_input == "no":
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Please type 'yes' or 'no'.")
