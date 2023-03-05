from FrenchDeck import Card, FrenchDeck
from random import choice

a = [1, 2, 3]
print(a[0])
print(a.__getitem__(0))

ranks = [str(n) for n in range(2, 11)] + list('JQKA')
print(ranks)

beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])
print(choice(deck))
print(choice(deck))
print(choice(deck))

for card in deck:
    print(card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print(rank_value)
    return rank_value * len(suit_values) + suit_values[card.suit]


print(spades_high(Card('2', 'clubs')))
print(spades_high(Card('A', 'spades')))

# for card in sorted(deck, key=spades_high):
#     print(card)
