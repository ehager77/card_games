import random
ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}
suits = ["clubs", "diamonds", "hearts", "spades"]
war_chest = []

# Card Class
# Takes rank, suit and value
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    def __str__(self):
        return str(self.rank) + ' of ' + self.suit
        
class Deck():
    def __init__(self):
        self.all_cards = []    
        for suit in suits:
            for rank in ranks:
                added_card = Card(rank, suit)
                self.all_cards.append(added_card)
                
    def shuffle_deck(self):
        random_nums = []
        
        while len(random_nums) != len(self.all_cards):
            rand_num = random.randint(0, len(self.all_cards) - 1)
            if rand_num in random_nums:
                pass
            else:
                random_nums.append(rand_num)
                
        for i, j in enumerate(random_nums):
            self.all_cards[i], self.all_cards[j] = self.all_cards[j], self.all_cards[i]
            
    def deal(self, player_one, player_two):
        while self.all_cards:
            player_one_card = self.all_cards.pop(0)
            player_one.cards.append(player_one_card)
            
            player_two_card = self.all_cards.pop(0)
            player_two.cards.append(player_two_card)
            
class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []

def check_for_win(player_1, player_2):    
    if len(player_1.cards) == 0:
        print(player_2.name + " wins the War!")
        print(player_1.name + " has been Decimated!!")
        return player_1.name  
    elif len(player_2.cards) == 0:
        print(player_1.name + " wins the War!")
        print(player_2.name + " has been Decimated!!")
        return player_2.name
    else:
        return False

def war(player_1, player_2): 
    global war_chest
    
    for i in range(0,4):
        try:
            war_chest.append(player_1.cards.pop(i))
            war_chest.append(player_2.cards.pop(i))
        except IndexError:
            continue
        
    for card in war_chest:
        print(card)
    print("There are " + str(len(war_chest)) + " cards in the war chest.")
    print("Player 1 now has " + str(len(player_1.cards)) + " cards")
    print("Player 2 now has " + str(len(player_2.cards)) + " cards")
    
    winner = play_game(player_1, player_2)
    
    if winner == player_1.name:
        while len(war_chest) != 0:
            player_1.cards.insert(-1, war_chest.pop(0))
        
    elif winner == player_2.name:
        while len(war_chest) != 0:
            player_2.cards.insert(-1, war_chest.pop(0))
            
    else:
        war(player_1, player_2)
                
def play_game(player_1, player_2):
    check_for_win(player_1, player_2)

    player_one_card = player_1.cards[0]
    player_two_card = player_2.cards[0]

    player_1_name = player_1.name.capitalize()
    player_2_name = player_2.name.capitalize()
    print(f"{player_1_name}'s Card: " + player_one_card.rank.capitalize() + " of " + player_one_card.suit.capitalize())
    print(f"{player_2_name}'s Card: " + player_two_card.rank.capitalize() + " of " + player_two_card.suit.capitalize())
    
    if player_one_card.value > player_two_card.value:
        print(player_1.name.capitalize() + " Wins!")
        player_1.cards.insert(-1, player_2.cards.pop(player_2.cards.index(player_two_card)))
        player_1.cards.insert(-1, player_1.cards.pop(player_1.cards.index(player_one_card)))
        print("Player 1 now has " + str(len(player_1.cards)) + " cards")
        print("Player 2 now has " + str(len(player_2.cards)) + " cards")
        return player_1.name
        
    elif player_two_card.value > player_one_card.value:
        print(player_2.name.capitalize() + " Wins!")
        player_2.cards.insert(-1, player_1.cards.pop(player_1.cards.index(player_one_card)))
        player_2.cards.insert(-1, player_2.cards.pop(player_2.cards.index(player_two_card)))
        print("Player 1 now has " + str(len(player_1.cards)) + " cards")
        print("Player 2 now has " + str(len(player_2.cards)) + " cards")
        return player_2.name
        
    elif player_two_card.value == player_one_card.value:
        print("WAR!!!")
        war(player_1, player_2)
        print("Player 1 now has " + str(len(player_1.cards)) + " cards")
        print("Player 2 now has " + str(len(player_2.cards)) + " cards")


def game_on():
    new_deck = Deck()
    new_deck.shuffle_deck()

    player_1_name = input("Hi Player 1! What's your name? ") 
    player_1 = Player(player_1_name)

    player_2_name = input("Hi Player 2! What's your name? ")
    player_2 = Player(player_2_name)

    new_deck.deal(player_1, player_2)

    print("LET'S PLAY!!")

    while not check_for_win(player_1, player_2):
        play_game(player_1, player_2)

game_on()


