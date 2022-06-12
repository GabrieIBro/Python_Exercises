from art import logo
import functions as fn
import random as rd
from time import sleep

print(logo)
sleep(1)

user_money = 500
rounds_played = 0

while True:

    # Variables
    rounds_played += 1
    all_cards = ('K', 'Q', 'J', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10)

    user_cards = [rd.choice(all_cards), rd.choice(all_cards)]
    pc_cards = [rd.choice(all_cards), rd.choice(all_cards)]

    sum_user = user_cards.copy()
    sum_user = fn.add(sum_user)

    sum_pc = pc_cards.copy()
    sum_pc = fn.add(sum_pc)

    # Player bet

    while True:
        print(f"\nYour balance: ${user_money}")
        bet = str(input('  Make a bet not greater than your balance:\n  > '))
        try:
            bet = int(bet)
        except ValueError:
            print('ONLY TYPE NUMBERS!')
        if type(bet) == int:
            if 1 <= bet <= user_money:
                break
            else:
                print('INVALID BET!')

    # Show players' cards

    print('\nDistributing cards', end='')
    for a in range(3):
        sleep(1)
        print('.', end='')
    sleep(0.8)

    print(f'\n\n  Your cards are: {user_cards}\n' + f"  Dealer's cards: [{pc_cards[0]}, *]")
    sleep(2)

    # Pick one more card

    while sum_user < 21:
        pick_card = str(input('\nDo you want one more card?\n  Type [Y] for Yes or [N] for No:\n  >')).upper().strip()
        if pick_card == 'Y':
            add = rd.choice(all_cards)
            user_cards.append(add)
            sum_user = user_cards.copy()
            sum_user = fn.add(sum_user)
            print(f"  The card {add} was added.")

        elif pick_card == 'N':
            break
        else:
            print("INVALID OPTION! ONLY TYPE 'N' OR 'Y'")

    # Show new cards

    sleep(0.5)
    print('\nNew hands:')
    sleep(0.5)
    print(f'\n  Your cards are: {user_cards}\n' + f"  Dealer's cards: {pc_cards}")

    while sum_pc < 17 and sum_user <= 21:
        pc_cards.append(rd.choice(all_cards))
        sum_pc = pc_cards.copy()
        sum_pc = fn.add(sum_pc)
        print(' '*17, pc_cards)
        sleep(1)

    # Verify winner

    won = True
    draw = False

    if sum_user == 21:
        print('  Blackjack! You won!')

    elif 21 >= sum_user > sum_pc:
        print('  You scored higher than the dealer! You won!')

    elif sum_user == sum_pc:
        print('  Draw!')
        draw = True

    elif sum_pc > 21:
        print('  The dealer bust! You won!')

    elif sum_user > 21:
        print('  Bust! You lost!')
        won = False

    elif 21 >= sum_pc > sum_user:
        print('  You lost!')
        won = False

    elif sum_pc == 21:
        print('  The dealer scored 21! You lost!')
        won = False

    if won is True and draw is False:
        user_money += (bet*2)
    elif won is False and draw is False:
        user_money -= bet

    # Verify if user is bankrupt or still want to play

    if user_money < 1:
        print("You're bankrupt! Game finished.")
        break

    keep_playing = str(input('\nDo you want to keep playing?\n  Type [Y] for Yes or [N] for No:\n  >')).upper().strip()

    if keep_playing == 'Y':
        continue
    elif keep_playing == 'N':
        break
    else:
        print('INVALID OPTION!')

print(f"Rounds played: {rounds_played}")
print(f"Your balance: ${user_money}")
print(f"Money earned: ${user_money - 500}")
