import random 


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):

        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards=[]
        suits=["heart","clubs","spades","diamonds"]
        ranks=[{"rank": "A","value": 11},
            {"rank": "K","value": 10},
            {"rank": "Q","value": 10},
            {"rank": "J","value": 10},
            {"rank": "2","value": 2},
            {"rank": "3","value": 3},
            {"rank": "4","value": 4},
            {"rank": "5","value": 5},
            {"rank": "6","value": 6},
            {"rank": "7","value": 7},
            {"rank": "8","value": 8},
            {"rank": "9","value": 9}]
        
        for i in suits:
                for j in ranks:
                    self.cards.append(Card(i,j))


    def shuffle(self):
        if len(self.cards)>1:
            random.shuffle(self.cards)


    def deal(self,number):
        cards_delt=[]
        for i in range (number):
            if len(self.cards)>0:
                card=self.cards.pop()
                cards_delt.append(card)
        
        return cards_delt

class Hand:
    def __init__(self,dealer=False):
        self.cards=[]
        self.value=0
        self.dealer=dealer
    def add_card(self,card_list):
        self.cards.extend(card_list)
    
    def calculate_value(self):
        self.value=0
        has_ace=False

        for i in self.cards:
            card_valu=int(i.rank["value"])
            self.value+=card_valu
            if i.rank["rank"]=="A":
                has_ace=True

        if has_ace and self.value>21:
            self.value-=10
    def get_valu(self):

        self.calculate_value()
        return self.value
    def isblackjack(self):
        return self.value==21
    
    def diplay(self,show_all_dealer_card=False):
        print(f''' {"Dealer's" if self.dealer else "yours "}    hand''')
        for index,i in enumerate(self.cards):
            if index==0 and self.dealer and not show_all_dealer_card and not self.isblackjack():
                print("hidden")
            else:
                print(i)
        if not self.dealer:
            print("value",self.get_valu())
            print()



class game:
    def play(self):
        game_number=0
        game_to_play=0
        while game_to_play <=0:

            try:
                game_to_play=int(input("how many game do you want to play"))
                
            except:
                print("you must enter a number here")

        while game_number < game_to_play:

            game_number+=1
            deck=Deck()
            deck.shuffle()

            player_hand=Hand()
            dealer_hand=Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
            print()
           
            print(f"game {game_number} of{game_to_play}")
            print("*" * 30)

            player_hand.diplay()
            dealer_hand.diplay()
            if self.check_winner(player_hand,dealer_hand):
                continue

            choice=""
            while player_hand.get_valu() <21 and choice not in["s","stand"]:
                choice=input("please choose hit or stand").lower()
                print()
                while choice not in ["s","h","stand","hit"]:
                    choice =input("please enter hit or stand or (h/s)").lower()
                    print()
                if choice in ["hit","h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.diplay()

            if self.check_winner(player_hand,dealer_hand):
                continue

            player_hand_valu=player_hand.get_valu()
            dealer_hand_valu=dealer_hand.get_valu()
            while dealer_hand_valu <17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_valu=dealer_hand.get_valu()
            dealer_hand.diplay(show_all_dealer_card=True)

            if self.check_winner(player_hand,dealer_hand):
                continue
            print("final result")
            print("your hand ",player_hand_valu)
            print("dealer hand",dealer_hand_valu)
            self.check_winner(player_hand,dealer_hand,True)
                
        print("tbkan you")




    def check_winner(self,player_hand,dealer_hand,game_over=False):
        if not game_over:

            if player_hand.get_valu() >21:
                print("you busted dealer win")
                return True
            elif dealer_hand.get_valu() >21:
                print("dealer busted you win")
                return True
            elif dealer_hand.isblackjack() and player_hand.isblackjack():
                print("tiee")
                return True
            elif player_hand.isblackjack():
                print(" you have black jack you win")
                return True
            elif dealer_hand.isblackjack():
                print("dealer win")
                return True
            
        else:
            if player_hand.get_valu() > dealer_hand.get_valu():
                print("you win")
            elif player_hand.get_valu() ==dealer_hand.get_valu():
                print("tie")
            else:
                print("dealer win")

        return False
            
    
        



            




g=game()
g.play()