from art import logo
from resources import resources, MENU
from time import sleep
from sys import exit

print(logo)


def check_resource(drink_type):
    """
    CHECK IF RESOURCES ARE AVAILABLE.
    """
    for key in MENU[drink_type]['ingredients']:
        if resources[key] < MENU[drink_type]['ingredients'][key]:
            print(f'INSUFFICIENT RESOURCES! Contact maintenance sector.')
            return 1


def insert_coin(coin):
    """
    COIN AMOUNT INPUT
    """
    while True:
        coin_amount = str(input(f"  How many {coin}?"))
        try:
            coin_amount = int(coin_amount)
            return coin_amount
        except ValueError:
            print('ONLY TYPE NUMBERS!\n')


# USER INPUT

while True:
    while True:
        drink_choice = str(input('\nChoose your drink:\n Espresso   - $1.50\n'' Latte      - $2.50\n'
                                 ' Cappuccino - $3.00\n >')).lower().strip()
        if drink_choice == '':
            print('TYPE SOMETHING!\n')
        elif drink_choice == 'espresso' or drink_choice == 'latte' or drink_choice == 'cappuccino' \
                or drink_choice == 'report':
            break
        else:
            print('INVALID OPTION!\n')

    # CHECK FOR RESOURCES AVAILABILITY OR PRINT REPORT
    availability = 0
    while True:

        if drink_choice != 'report':
            availability = check_resource(drink_choice)
            if availability == 1:
                break
        else:
            for item in resources:

                if item != 'coffee':
                    print(f" {item.title()}: {resources[item]}ml")
                else:
                    print(f" {item.title()}: {resources[item]}g")

            turn_off = str(input(' >')).lower().strip()

            if turn_off == 'off':
                exit()
            else:
                break

        # PAYMENT: ONLY SHOW SMALLER VALUES IF TOTAL AMOUNT IS LESSER THAN DRINK COST
        print(f"\n Drink cost: ${MENU[drink_choice]['cost']:.2f}")

        total_value = 0

        quarter = insert_coin('quarters')
        total_value += (quarter * 0.25)

        if total_value < MENU[drink_choice]["cost"]:
            dime = insert_coin('dimes')
            total_value += (dime * 0.10)

            if total_value < MENU[drink_choice]["cost"]:
                nickel = insert_coin('nickels')
                total_value += (nickel * 0.05)

                if total_value < MENU[drink_choice]["cost"]:
                    penny = insert_coin('pennies')
                    total_value += (penny * 0.01)

        # VERIFY PAYMENT AND DEDUCT RESOURCES

        if total_value < MENU[drink_choice]['cost']:
            print(f"You only inserted ${total_value:.2f}.\n Refunding money... ")

        else:
            print(f"\nYOUR CHANGE: ${(total_value-MENU[drink_choice]['cost']):.2f}", '\nMaking drink', end='')

            for item in resources:
                resources[item] -= MENU[drink_choice]['ingredients'][item]
                sleep(1)
                print('.', end='')

        # VERIFY IF THE USER WANT TO RUN THE PROGRAM AGAIN
        while True:
            run_again = str(input('\nDo you want to buy another drink? Type:\n [Y] Yes\n [N] No\n >')).strip().upper()
            if run_again == '':
                print('TYPE SOMETHING!')
            elif run_again in 'YES':
                break
            elif run_again in 'NO':
                exit()
            else:
                print('INVALID OPTION!')

        if run_again in 'YES':
            break
