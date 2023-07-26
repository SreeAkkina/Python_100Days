import os

os.system('cls')

cont = "yes"
auction = {}
max_bid = 0
max_bidder = ""

while cont == "yes":
    name = input("What is your name? >>> ")
    bid = int(input("What is your bid? >>> $"))
    auction[name] = bid

    cont = input("Would you like to continue(yes or no)? >>> ")
    os.system('cls')

for key in auction:
    if auction[key] > max_bid:
        max_bid = auction[key]
        max_bidder = key


print(f"The winner is {max_bidder} with a bid of ${max_bid}")