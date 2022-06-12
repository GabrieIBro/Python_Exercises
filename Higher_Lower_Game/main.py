from gamedata import data
from art import logo, vs
from random import sample
from time import sleep
print(logo)

index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
         26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]

a = b = rounds = 0


def user_answer():
    while True:
        a_or_b = str(input('Who has more followers? Type "A" or "B": ')).strip().upper()
        if a_or_b == 'A' or a_or_b == 'B':
            return a_or_b
        else:
            print("INVALID OPTION!")


while True:

    if rounds < 1:
        a = sample(index, k=1)[0]
        index.remove(a)

        b = sample(index, k=1)[0]
        index.remove(b)

    rounds += 1

    sleep(1)
    print(f"\nROUND {rounds}"+'\n\nA: ', end='')
    for key in data[a]:
        if type(data[a][key]) != int:
            print(data[a][key], end=', ')
    print('\b\b\n' + vs + '\nB: ', end='')

    for key in data[b]:
        if type(data[b][key]) != int:
            print(data[b][key], end=', ')
    print('\b\b\n')

    answer = user_answer()

    if answer == 'A':
        if data[a]['follower_count'] > data[b]['follower_count']:
            b = sample(index, k=1)[0]

        else:
            print('YOU LOST!')
            break

    if answer == 'B':
        if data[b]['follower_count'] > data[a]['follower_count']:
            a = sample(index, k=1)[0]

        else:
            print('YOU LOST!')
            break
