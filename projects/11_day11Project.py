#blackjack project
import random
import os

os.system("cls")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def selectcards(num):
    list = []
    for x in range(num):
        list += random.choice(cards)
    return list

def score(list):
    total = 0
    for x in list:
        total += list[x]
    return total

print("Welcome to Blackjack!!")
cont = True
playerScore, dealerScore = 0, 0

while cont:
    playerCards = selectcards(2)
    dealerCards = selectcards(2)
    playerScore += score(playerCards)
    dealerScore += score(dealerCards)

    
    
