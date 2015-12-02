from card import Card, BuildingCard, CardType, CardName
from player import Player
from players import DoNothingPlayer, BuyGoldenPlayer
import random

class Game:

    players = []
    board = []
    winner = None
    round_number = 0
    
    def initialize_game(self):
        # initiate game with two players   
        player_names = ["Al", "So"]
    
        for i in range (0,6):
            self.board.append(BuildingCard(CardName.BAKERY, 1, CardType.GREEN, [2,3], 1))
            self.board.append(BuildingCard(CardName.FARM, 1, CardType.BLUE, [2], 1))
            self.board.append(BuildingCard(CardName.WHEAT_FIELD, 1, CardType.BLUE, [1], 1))
            self.board.append(BuildingCard(CardName.CAFE, 2, CardType.RED, [3], 1))
            self.board.append(BuildingCard(CardName.MINI_MARKET, 2, CardType.GREEN, [4], 3))
            self.board.append(BuildingCard(CardName.FOREST, 3, CardType.BLUE, [5], 1))
            self.board.append(BuildingCard(CardName.MINE, 6, CardType.BLUE, [9], 5))
            self.board.append(BuildingCard(CardName.MILK_FACTORY, 5, CardType.GREEN, [7], 0))
            self.board.append(BuildingCard(CardName.FURNITURE_FACTORY, 3, CardType.GREEN, [8], 0))
            self.board.append(BuildingCard(CardName.FAMILY_RESTAURANT, 3, CardType.RED, [9,10], 2))
            self.board.append(BuildingCard(CardName.MALL, 2, CardType.GREEN, [11,12], 0))
            self.board.append(BuildingCard(CardName.PLANTATION, 3, CardType.BLUE, [10], 3))
        
        for name in player_names:
            # Purple cards are only one per player
            self.board.append(BuildingCard(CardName.STADIUM, 6, CardType.PURPLE, [6], 0))
            self.board.append(BuildingCard(CardName.TELEVISION_TOWER, 7, CardType.PURPLE, [6], 0))
            self.board.append(BuildingCard(CardName.OFFICE_BUILDING, 8, CardType.PURPLE, [6], 0))
    
            # Golden cards are considered to be on the board, but each player can only buy one of them
            self.board.append(BuildingCard(CardName.TRAIN_STATION, 4, CardType.GOLDEN, [], 0))
            self.board.append(BuildingCard(CardName.SHOPPING_MALL, 10, CardType.GOLDEN, [], 0))
            self.board.append(BuildingCard(CardName.AMUSEMENT_PARK, 16, CardType.GOLDEN, [], 0))
            self.board.append(BuildingCard(CardName.RADIO_TOWER, 22, CardType.GOLDEN, [], 0))

            if name == "Al":    
                player = DoNothingPlayer(name)
            else:
                player = BuyGoldenPlayer(name)
            
            player.buy_card(BuildingCard(CardName.BAKERY, 0, CardType.GREEN, [2,3], 1))
            player.buy_card(BuildingCard(CardName.WHEAT_FIELD, 0, CardType.BLUE, [1], 1))
            
            player.take_coins(3)
            
            self.players.append(player)
            
    def play_game(self):
        while (self.winner == None) and (self.round_number < 1000):
            print "starting round " + str(self.round_number)
            self.round_number += 1
            self.play_round()
            
        if self.winner:
            print "winner is player " + self.winner.name
        else:
            print "no winner :("
        
    def play_round(self):
        for player in self.players:
            self.play_turn(player)
        
            
    def play_turn(self, player):
        #print "playing turn for " + player.name
        
        if (player.has(CardName.TRAIN_STATION)):
            number_of_dice = self.ask_number_dice(player)
        else:
            number_of_dice = 1
        
        result = self.roll(player, number_of_dice)
        
        if (player.has(CardName.AMUSEMENT_PARK)):
            wants_repeat = self.ask_repetition(player)
            if (wants_repeat):
                result = self.roll(player, number_of_dice)
        
        self.handle_result(result, player)
        
        action = player.choose_action(self)
        
        self.perform_action(action, player)
            
        if (player.has_all_gold_cards()):
            print "We have a winner!"
            self.winner = player
        elif (player.has(CardName.RADIO_TOWER) and result[0] == result[1]):
            play_turn(player)
        
    def ask_number_dice(self, player):
        return 1
    
    def ask_repetition(self, player):
        return False
        
    def perform_action(self, action, player):
        if action:
            print "performing"
        if action is not None:
            print "Player " + player.name + " wants to buy " + action
            available = [x for x in self.board if x.card_name == action]
            print "There are " + str(len(available)) + " left"
            if len(available) == 0:
                raise ValueError('Invalid Operation: Buy a card that is not in the board')
            print available[0].card_name
            card = self.board.pop(self.board.index(available[0]))
            player.buy_card(card)
    
    def handle_result(self, result, player):
        #print "handling result " + str(result) + " for player " + player.name
                
        for card in player.playing_area:
            if card.is_active:
                card.activate(player, result)
            
        
    def roll(self, player, number_of_dice):
        result = []
        result.append(self.roll_one_die())
        if (number_of_dice == 2):
            result.append(self.roll_one_die())
        return result
        
    def roll_one_die(self):
        return int(random.randint(1,6))

