
from classes.deck import Deck
import random



class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    
    def __repr__(self):
        return f'{self.name, self.hand}'

    def deal_card(self, deck = Deck()):
        idx = random.randint(0, len(deck.cards)-1)
        card = deck.cards[idx]
        self.hand.append(card)
        deck.cards.pop(idx)
        return self
        #could also do random.shuffle(deck.cards)
    
    def total(self):
        sum = 0
        for card in self.hand:
            sum += card.point_val
        return sum
