print("Welcome to Treasure Island. Your mission is to find the treasure!")

direction = input("Would you like to go left or right >>> ").lower()

if direction == "left":
    swim = input("Would you like to swim or wait >>> ").lower()
    if swim == "wait":
        door = input("Which door would you like to pass through (red, yellow, or blue) >>> ").lower()
        if door == "yellow":
           print("YOU WIN!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")