from random import sample

print('NUMBER GUESSING GAME')


def dif_level():
    difficulty = str(input('\nType the desired difficulty:\n[E] ─ Easy\n[M] ─ Medium\n[H] ─ Hard\n>')).strip().upper()
    chances = 0

    if difficulty in 'EASY':
        chances = 15
    elif difficulty in 'MEDIUM':
        chances = 10
    elif difficulty in 'HARD':
        chances = 5

    if difficulty not in 'EASYMEDIUMHARD' or difficulty == '':
        print('INVALID OPTION!')
        dif_level()

    return chances


attempts = dif_level()
print(f"You have {attempts} chances!", "\n\nThe computer picked a number!")

number = sample(range(100), k=1)


while attempts != 0:
    attempts -= 1

    while True:
        user_guess = str(input('What is you guess? '))
        try:
            user_guess = int(user_guess)
            break
        except ValueError:
            print('ONLY TYPE NUMBERS!')

    if user_guess == number[0]:
        print("\nYou guessed correctly")
        break
    elif user_guess > number[0]:
        print(f"Too high! Try again.\n{attempts} attempts left.\n")
    elif user_guess < number[0]:
        print(f"Too low! Try again.\n{attempts} attempts left.\n")