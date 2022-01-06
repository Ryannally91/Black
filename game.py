from classes.deck import Deck
import random


bicycle = Deck()

bicycle.show_cards()

for card in bicycle.cards:
    if card.string_val in ['Jack', 'Queen', 'King']:
        card.point_val = 10
    if card.string_val =='Ace':
        card.point_val = [1, 11]
        # ask via input for use to choose (how to program for computer)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        # return self
    
    def __repr__(self):
        return f'{self.name, self.hand}'

    def deal_card(self):
        idx = random.randint(0, len(bicycle.cards)-1)
        card = bicycle.cards[idx]
        self.hand.append(card)
        bicycle.cards.pop(idx)
        return self
    
    def total(self):
        sum = 0
        for card in self.hand:
            sum += card.point_val
        print(sum)
        return sum


#Black jack
# to-do:  create computer deal,  winner function, ace = 1 or 11
num_of_players = int(input('Number of Players: '))

def create_players(num_of_players):
    players = []  
    for i in range(num_of_players):
        if i ==0:
            players.append(Player('human'))
        else:
            players.append(Player(f'player_{i}'))
    return players

def deal(players):
    for player in players:
        for i in range(2):
            player.deal_card()
        print(player.hand[0])
    print(players[0].hand)

#comp function (if value of cards <14 append 1 card)
def comp_choice(players):
    for player in players[1:]:
        sum=0
        for card in player.hand:
            sum+= card.point_val
        if sum <15:
            player.deal_card()
            comp_choice(players)

def hit_or_stay(players):
    answer=input('Hit or Stay (type hit or stay): ').lower()
    if answer not in ['hit', 'stay']:
        print('enter either "hit" or "stay"')
        hit_or_stay(players)
    else:
        if answer == 'hit':
            players[0].deal_card()
            print(players[0].hand)
            hit_or_stay(players)
        else: 
            comp_choice(players)
            declare_winner(players)

def declare_winner(players):
    contenders = []
    for player in players:
        print(f'{player.name} has {player.hand}')
        total= player.total()
        if total <= 21:
            contenders.append(total)
    # for total in contenders:
    #     winner = 

def main():
    players = create_players(num_of_players)
    deal(players)
    
    hit_or_stay(players)

main()

'''
Blackjack
1)number of players (plus dealer?)-use input('number of players: ')
create player class?
2)deal function:  Math random to correspond with a number in deck, 
then eliminate that card from list,  use for loop len(int(players))
3) how to have one card visible and other hidden
4)Prompt each player to 'hit' or 'stay'.  (have decicion-algorithm for computer players )
pointvalues: use inheritance but superceede point values for face cards,  Ace (if statement, total over 21 then ace= 1)
5) end round--display player total
    logic:  
    if player1 total > 21:
        print('Bust')
    elif player1 total == 21:
        print('blackjack! You win')
    else: 
        print(f{winner})
    
    def contenders:
        contenders:[]
        for player in players:
            if player score < 21:
                contenders.append(player)
        return contenders

    def winner:
        winner = 0
        for player in contenders:
            if player score > winner:
                winner = player 
        #need case for ties
'''



'''Takeaways from assignment:

-instance methods vs. putting functions in main
-generating players-- utilizing a list and appending objects to it
-for loops using indexs vs elements
for i in range(len(list))
    list[i] = ...
vs.

for each in list:
    each.append(...)   (this being ore effective)

-not subscriptive (us it reading it as an object).  The deal function, having variable for index and card, pop, etc. helped with read ability and understanding
-when I noticed repeated code for dealing cards, I make a class method for it(deal_card)

'''
