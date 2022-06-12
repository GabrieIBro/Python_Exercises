import random as rd
from time import sleep
from word_list import words, hangman

print("""                                                
          /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __   
         / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  
        / __  / (_| | | | | (_| | | | | | | (_| | | | | 
        \/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                           |___/                        \n""")

# Variables

attempts = wrong_guess = print_word = 0
pick_word = list(rd.choice(words))
underscores = []
copy_pickword = pick_word.copy()
letters = []

for a in range(0, len(pick_word)):
    underscores.append('＿')

print('      The computer chose a word! Try to guess its letters:')
sleep(3)

while True:
    # Show picked word
    attempts += 1
    if attempts == 1:
        print_word = underscores.copy()

    print(hangman[wrong_guess], '\nWord: ', end='')

    for items in print_word:
        print(items, end='')

    print(f'\nUsed letters: {letters}')
    # User input
    while True:
        user_guess = str(input(f'\nAttempt {attempts}: ')).lower().strip()
        if user_guess.upper() in letters:
            print('You already chose this letter!')
        elif len(user_guess) == 1 and not user_guess.isnumeric():
            letters.append(user_guess.upper())
            break
        elif user_guess.isnumeric():
            print('Error! You typed a number instead of a letter!')
        else:
            print('\nError! You typed more than one letter!')

    # Verify if the user guessed correctly
    if user_guess in pick_word:
        for letter in pick_word:
            if letter == user_guess:
                index = (pick_word.index(letter))
                pick_word[index] = '0'
                print_word[index] = letter
                print('YOU GUESSED THE CORRECTLY!')
    else:
        wrong_guess += 1
        print('YOU GUESSED WRONG!')
    sleep(1)
    # Verify if the user lost or won
    if wrong_guess == 6:
        print(hangman[6], f'\nThe word was: {"".join(map(str, copy_pickword)).replace(",", "").title()}', '\nYOU LOST!')
        break

    elif print_word == copy_pickword:
        print(f'\nThe word was: {"".join(map(str, copy_pickword)).replace(",", "").title()}', '\nYOU WON!')
        break

