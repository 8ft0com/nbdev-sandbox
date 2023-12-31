# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/apps/poker/01_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ../nbs/apps/poker/01_deck.ipynb 3
from .card import *

# %% ../nbs/apps/poker/01_deck.ipynb 4
class Deck:
    "A Deck of cards"
    def __init__(self): self.cards = [Card(suit, rank) for suit in range(4) for rank in range(1,14)]
    def __str__(self): return '; '.join(map(str, self.cards))

    # def __init__(self, cards): S.cards = list(cards)
    def __len__(self): return len(self.cards)
    def __getitem__(self, i): return self.cards[i]
    def __setitem__(self, i, c): self.cards[i] = c
    def __delitem__(self, i): del self.cards[i]
    def __repr__(self): return f'{self.__class__.__name__} ({len(self)} cards)'
    def pop(self, i=-1): return self.cards.pop(i)
    def add(self, card): self.cards.append(card)
    def shuffle(self): random.shuffle(self.cards)
    def sort(self): self.cards.sort()
    def move(self, card, to):
        if not isinstance(card, Card): card = Card(card)
        if not isinstance(to, Deck): to = Deck(to)
        self.cards.remove(card)
        to.add(card)
