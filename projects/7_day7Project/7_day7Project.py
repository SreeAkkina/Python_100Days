import random
import art
import words

print(art.logo)
print("Welcome to Hangman")

word = random.choice(words.word_box)
word_list = []
chosen_letters = []

for n in word:
    word_list.append("_")
    #can also use word_list += "_"
print(word_list)
print("")

cont = True
lives = 6

while cont:
    letter_guess = input("Guess a Letter >>> ").lower()

    if letter_guess in chosen_letters:
        print("You have already chosen this letter")
        continue
    chosen_letters.append(letter_guess)

    for x in range(len(word)):
        letter = word[x]
        if letter_guess == letter:
            word_list[x] = letter
    print(word_list)
    
    if letter_guess not in word:
        print("Your guess is not in the word\n")
        lives -= 1
        if lives == 0:
            print(f"The word was {word}")
            print("You LOSE")
            cont = False
    if "_" not in word_list:
        print("You WIN")
        cont = False
    print("------------------------------")
    print(art.stages[lives])

        

