from classes.deck import Deck
from classes.player import Player


bicycle = Deck()

for card in bicycle.cards:
    if card.string_val in ['Jack', 'Queen', 'King']:
        card.point_val = 10
    if card.string_val =='Ace':
        card.point_val = 11
        
#Black jack
num_of_players = int(input('Number of Players: '))
name = input('Name: ')

def create_players(num_of_players):
    players = []  
    for i in range(num_of_players):
        if i ==0:
            players.append(Player(name))
        else:
            players.append(Player(f'player_{i}'))
    return players

def deal(players):
    for player in players:
        for i in range(2):
            player.deal_card(bicycle)
        print(player.name, player.hand[0])
    print(players[0].hand)

def comp_choice(players):
    for player in players[1:]:
        sum = player.total()
        if sum <15:
            player.deal_card(bicycle)
            comp_choice(players)

def hit_or_stay(players):
    answer=input('Hit or Stay (type hit or stay): ').lower()
    if answer not in ['hit', 'stay']:
        print('enter either "hit" or "stay"')
        hit_or_stay(players)
    else:
        if answer == 'hit':
            players[0].deal_card(bicycle)
            print(players[0].hand)
            _total = players[0].total()
            if _total > 21 and 'Ace' not in players[0].hand:
                #bug: not detecting ace
                print(players[0].hand)
                print('busted')
                declare_winner(players)
            else:
                hit_or_stay(players)
        else: 
            for card in players[0].hand:
                if card.string_val == 'Ace':
                    ace_value = int(input('Ace is 11 or 1: '))
                    card.point_val = ace_value
            comp_choice(players)
            declare_winner(players)

def declare_winner(players):
    scores = []
    for player in players:
        print(f'{player.name} has {player.hand}')
        total= player.total()
        if total <= 21:
            scores.append({'name' : player.name, 'score' : total})
    scores = sorted(scores, key= lambda i: i['score'])
    # need case for a tie
    for player in scores[0:-1]:
        if player['score'] == scores[len(scores)-1]['score']:
            print(f'{player["name"]} and {scores[len(scores)-1]["name"]} are the winners')
            break
    print(scores[len(scores)-1]['name'] , ' is the winner')

def main():
    players = create_players(num_of_players)
    deal(players)
    hit_or_stay(players)

main()



#extensions: Add money wager component or scoring system per round, cash out feature

