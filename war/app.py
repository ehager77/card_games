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
        self.won_cards = []