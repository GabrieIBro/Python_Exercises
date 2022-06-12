print('CAESAR CIPHER\n')

letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z')

while True:
    while True:

        # User Input

        encode_or_decode = str(input("Type [0] to encode, type [1] to decode:\n>"))
        if encode_or_decode in '01' and len(encode_or_decode) == 1:
            encode_or_decode = int(encode_or_decode)
            break
        else:
            print('INVALID OPTION!')

    while True:
        shift = str(input('Type how many times you want to shift the letters:')).strip()
        if shift.isnumeric():
            shift = int(shift)
            if shift > 26:
                print('TYPE NUMBERS LESS THAN 26!')
            else:
                break
        else:
            print('ONLY TYPE POSITIVE INTEGER NUMBERS!')

    text = list(str(input("\nWrite a message: ")).upper())

    # Grab index of each letter

    text_indexes = []
    for letter in text:
        if letter in letters:
            text_indexes.append(letters.index(letter))
        elif ValueError:
            text_indexes.append(letter)

    # Verify if the message will  be encoded or decoded | Shift index

    for pos, index in enumerate(text_indexes):
        if type(index) == int:
            if encode_or_decode == 0:
                add = index + shift

                if add > 25:
                    add -= 26
                    text_indexes[pos] = add
                else:
                    text_indexes[pos] = add

            else:
                add = index - shift

                if add < 0:
                    add += 26
                    text_indexes[pos] = add
                else:
                    text_indexes[pos] = add

    # Print word

    if encode_or_decode == 0:
        print('Encoded text: ', end='')
    else:
        print('Decoded text: ', end='')

    for index in text_indexes:
        if type(index) == int:
            print(letters[index], end='')
        else:
            print(index, end='')

    # Run again
    while True:
        run_again = str(input("\n\nType 'YES' to run again or 'X' to finish: \n")).upper().strip()
        if run_again in 'YESX':
            break
        else:
            print('Invalid option!')

    if run_again == 'X':
        break
    else:
        continue
