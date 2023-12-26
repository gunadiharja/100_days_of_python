from banner import ascii

print(ascii)

print("Welcome to Treasure Island!\nYou're mission is to find the treasure.\n")

opt1 = input(
    "You're at a crossroad. Where do you want to go? Type \"left\" or \"right\"\n> ")
if opt1.lower() == "left":
    opt2 = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n> ")
    if opt2.lower() == "wait":
        opt3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n> ")
        if opt3.lower() == "blue":
            print("You enter a room of beasts. Game Over.")
        elif opt3.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif opt3.lower() == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("Game over!")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
    