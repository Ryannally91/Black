
from classes.deck import Deck
from classes.player import Player


bicycle = Deck()
human = Player('Human')
comp = Player('computer')

def initial_deal():
    while(len(bicycle.cards) > 0):
        human.deal_card(bicycle)
        comp.deal_card(bicycle)

def play_round():
    hum_card = human.hand.pop(0)
    # print(hum_card)
    comp_card= comp.hand.pop(0)
    # print(type(comp_card))
    show = [hum_card, comp_card]
    if hum_card.point_val > comp_card.point_val:
        for card in show:
            human.hand.append(card)
            return human.hand
    elif hum_card.point_val == comp_card.point_val:
        for i in range(3):
            show.append(hum_card)
            show.append(comp_card)
        if show[5].point_val > show[6].point_val:
            for card in show:
                human.hand.append(card)
                return human.hand
        else:
            for card in show:
                comp.hand.append(card)
                return comp.hand
            
    else: 
        for card in show:
            comp.hand.append(card)
            return comp.hand

def main():
    initial_deal()
    while len(human.hand) !=0 or len(comp.hand) != 0:
        play_round()
    if len(human.hand) != 0:
        print('You win')
    else:
        print('computer wins')
main()

"""
Implement the card game war. Rules are:

1. Deal out deck of 52 cards between two users.
2. Each player plays a card. Higher card wins. Winner takes both cards.
3. If players tie, then each player puts down three cards, and the third
   card competes.
   If a player has less than 3 cards, then they put down all of their cards
   and their final card competes against the other player's third card.
   Continue doing this until tie is broken.
   Winner takes all cards.
4. Game is over when a player doesn't have any cards. The player with
   cards remaining is the winner.
"""

'''
Pseudo
1. generate Deck,  create instances of players

2. deal out deck between two users (human vs, comp)
--- call deal_card fuction while deck > 0
def initial_deal():
    while(len(bicycle.cards) > 0):
        human.deal_card(bicycle)
        comp.deal_card(bicycle)

3. round function 
def play_round():
    hum_card = human.hand.pop()
    print(hum_card)
    comp_card= comp.hand.pop()
    print(comp_card)

take from back of list,
compare cards, if tie take three  cards 
use range in 3 and pop 

 winner adds both cards to front of list (prepend?)

while (len(human.hand) !=0 or len(comp.hand) != 0):
    play_round():
'''