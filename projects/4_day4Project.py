import random

rps = ["rock", "paper", "scissors"]

comp_choice = rps[random.randint(0,2)]
user_choice = input("Please enter rock, paper, or scissors >>> ").lower()

print(f"You chose {user_choice} and the computer chose {comp_choice}")

if comp_choice == user_choice:
    print("Tie")
elif comp_choice == "rock" and user_choice == "paper":
    print("You win")
elif comp_choice == "paper" and user_choice == "rock":
    print("You lose")
elif comp_choice == "scissors" and user_choice == "paper":
    print("You lose")
elif comp_choice == "paper" and user_choice == "scissors":
    print("You win")
elif comp_choice == "rock" and user_choice == "scissors":
    print("You lose")
elif comp_choice == "scissors" and user_choice == "rock":
    print("You win")




