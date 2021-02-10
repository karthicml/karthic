import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]  
    def __str__(self):
        return self.rank + " of " +self.suit
class Deck:
    def __init__(self,decks=1):
        self.all_cards = []
        for i in range(decks):
            for suit in suits:
                for rank in ranks:
                    created_card = Card(suit,rank)
                    self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
class Player:
    def __init__(self,name):
        self.name = name
        self.player_cards = []
    def remove_one(self):
        return self.player_cards.pop(0)
    def add_cards(self,new_cards):
        self.player_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name}'
class Dealer:
    def __init__(self):
        self.dealer_cards = []
    def remove_one(self):
        return self.dealer_cards.pop(0)
    def add_cards(self,new_cards):
        self.dealer_cards.append(new_cards)
    def __str__(self):
        return f'Dealer has {len(self.dealer_cards)} cards'
def deck_func():
    deck = 1
    isint1 = True
    while isint1:
        a = input('Enter the number of decks between 1 - 5 : ')
        try:
            if isinstance(int(a),int)==True and 0 < int(a) < 6:
                deck = int(a)
                isint = False
                return deck
        except:
            pass
def deal_open(player1):
    player1.add_cards(newdeck.deal_one())
    print('{} - Your card no.1: {}' .format(player1,player1.player_cards[0]))
    player1.add_cards(newdeck.deal_one())
    print('{} - Your card no.2: {}' .format(player1,player1.player_cards[1]))  
    dealer.add_cards(newdeck.deal_one())
    print('Dealer card no.1: {}' .format(dealer.dealer_cards[0]))
    dealer.add_cards(newdeck.deal_one())
    print('Dealer card no.2: Hidden')
def buy_in():
    buy_in = 0
    isint2 = True
    while isint2:
        b = input('Enter your buy in amount (min $100 / max $5,000) :')
        try:
            if isinstance(int(b),int)==True and 100 <= int(b) <= 5000 :
                buy_in = int(b)
                return buy_in
        except:
            pass
def bet_size():
    bet_size = 100
    isint3 = True
    while isint3:
        c = input('Enter your bet amount ($100 minimum / X 100) : ')
        try:
            if 100 <= int(c) <= 5000 and int(c)%100 ==0:
                bet_size = int(c)
                return bet_size
        except:
            print('Enter a bet amount in multiples of 100 ($100 minimum)')
def insuf_limit(limit,game_on):
    while True: 
        if limit<100:
            in1 = input('Insufficent buying power! Do you want to add funds? (Y/N): ')
            if in1 == 'y' or in1 == 'Y':
                add_fund = buy_in()
                limit+=add_fund
                while limit>=100:
                    return [limit,True]
            elif in1 == 'n' or in1 == 'N':
                print('Game Over!')
                return [limit,False]
            else:
                print('Please enter only Y or N')
        else:
            return [limit,True]
def bet_check(limit,bet_amount):
    while True:
        if 100<=limit and limit<bet_amount:
            print('Insufficient funds. Your balance is {}'.format(limit))
            in2 = input('Enter 1 to add funds, 2 to place smaller bet, 3 to quit : ')
            if in2 =='1':
                add_fund = buy_in()
                limit+=add_fund
                while limit>=bet_amount:
                    return [limit,bet_amount,True]
            elif in2 =='2':
                temp1 = bet_size()
                while temp1>limit:
                    temp1 = bet_size()
                bet_amount = temp1
                return [limit,bet_amount, True]
            elif in2 =='3':
                bet_amount = 0
                print('Game Over!')
                return [limit,bet_amount, False]
            else:
                print('Enter only 1, 2 or 3')
        elif limit<100:
            print('Insufficient funds. Your balance is {}'.format(limit))
        else:
            return [limit,bet_amount,True]
def bustornot(limit,bet_amount):
    length = len(player1.player_cards)
    points = 0
    ace_count = 0
    for i in range(length):
        points+= player1.player_cards[i].value
        if player1.player_cards[i].rank == 'Ace':
            ace_count +=1
        if ace_count == 2:
            print('You have 2 Aces. You can choose either 1 or 11 points for this card')
            points-=10
    print(f'Value of your cards is ' +str(points))
    while points<21:
        while True:
            in3 = input('Enter 1 for Hit or 2 for Stay: ')
            if in3 == '1':
                player1.add_cards(newdeck.deal_one())
                new_len = len(player1.player_cards)
                points = 0
                ace_count = 0
                for i in range(new_len):
                    print('{} - Your card no{}: {}' .format(player1,i+1,player1.player_cards[i]))
                    points+= player1.player_cards[i].value
                    if player1.player_cards[i].rank == 'Ace':
                        ace_count +=1
                        print('You have {}. You can choose either 1 or 11 points for this card'.format(player1.player_cards[i]))
                if points>21 and ace_count>0:
                    points-=10
                print(f'Value of the cards is ' +str(points))     
                break        
            elif in3 == '2':
                dealer_len = len(dealer.dealer_cards)
                dealer_points =0
                for i in range(dealer_len):
                    dealer_points+= dealer.dealer_cards[i].value
                if dealer.dealer_cards[i].rank == 'Ace':
                    ace_count +=1
                if ace_count == 2:
                    dealer_points-=10
                if dealer_points ==21:
                    print('Dealer points is {}. Dealer Wins.' .format(dealer_points))
                    return limit
                while dealer_points<21:
                    while True:
                        if dealer_points>points:
                            for i in range(dealer_len):
                                print('Dealer card no{}: {}' .format(i+1,dealer.dealer_cards[i]))
                            print('Dealer points is {}. Dealer Wins!' .format(dealer_points))
                            return limit
                        elif dealer_points == points:
                            for i in range(dealer_len):
                                print('Dealer card no{}: {}' .format(i+1,dealer.dealer_cards[i]))
                            print('Dealer points is {}. Game Draw!' .format(dealer_points))
                            return (limit+bet_amount)
                        else:
                            dealer.add_cards(newdeck.deal_one())
                            dealer_len = len(dealer.dealer_cards)
                            dealer_points = 0
                            ace_count = 0
                            for i in range(dealer_len):
                                dealer_points+= dealer.dealer_cards[i].value
                                #print('Dealer card no{}: {}' .format(i+1,dealer.dealer_cards[i]))
                                if dealer.dealer_cards[i].rank == 'Ace':
                                    ace_count +=1
                                if dealer_points>21 and ace_count>0:
                                    dealer_points-=10
                                elif dealer_points>21:
                                    for i in range(dealer_len):
                                        print('Dealer card no{}: {}' .format(i+1,dealer.dealer_cards[i]))
                                    print('Dealer busts! Dealer points is {}. You win!' .format(dealer_points))
                                    return (limit+bet_amount*2)
                                else:
                                    pass
                
            else:
                print('Please enter only 1 or 2')     
    if points == 21:
        print('BlackJack!!! You Win!')
        pot = limit + bet_amount*2.5
        return pot
    else:
        print('You Bust! Dealer Wins!')
        return limit 
def quit_game(player1):
    while True:
        quit_game = input('Enter Y to quit game or N to play more : ')
        if quit_game == 'y' or quit_game == 'Y':
            print('Game Over!')
            return False
        elif quit_game == 'n' or quit_game == 'N':
            player1.player_cards = []
            dealer.dealer_cards = []
            return True
        else:
            print('Please enter only Y or N')
player1 = Player(input('Enter your name: '))
dealer = Dealer()
player1.player_cards = []
dealer.dealer_cards = []
decks_played = deck_func()
newdeck = Deck(decks_played)
newdeck.shuffle()
limit = buy_in()
game_on = True
round_num = 0
while game_on:
    chk_lim = insuf_limit(limit,game_on)
    limit =chk_lim[0]
    game_on = chk_lim[1]
    if game_on == True:
        bet_amount = bet_size()
        chk_bet = bet_check(limit,bet_amount)
        limit = chk_bet[0]
        bet_amount = chk_bet[1]
        game_on = chk_bet[2]
    if game_on == False: 
        break
    round_num +=1
    print(f'Round {round_num}') 
    limit-=bet_amount
    print('{} - your bet amount is {} and remaining limit is {}'.format(player1,bet_amount,limit))
    deal_open(player1)
    new_limit = bustornot(limit,bet_amount)
    limit = new_limit
    print('Your limit is now {}' .format(limit))
    print('Remaining cards in deck are {}'.format(len(newdeck.all_cards)))
    if len(newdeck.all_cards)<26:
        newdeck = Deck(decks_played)
        newdeck.shuffle()
        print('Deck has been reset')
    game_on = quit_game(player1)