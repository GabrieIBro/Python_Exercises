def add(cards):
    """
    :param cards: Player's and dealer's hand
    :return: Result of the addition of the cards
    """
    for pos, item in enumerate(cards):
        if type(item) == str and item != 'A':
            cards[pos] = 10
        elif item == 'A':
            cards[pos] = 11

    for pos, item in enumerate(cards):
        if item == 11 and sum(cards) > 21:
            cards[pos] = item - 10

    cards = sum(cards)
    return cards
