from card import Card, BuildingCard, VictoryCard, CardType
from player import Player

players = []
board = []

def initialize_game():
    # initiate game   
    player_names = ["Al", "So"]
    players = []
    board = []
 
    for i in range (0,6):
        board.append(BuildingCard("bakery", 1, CardType.GREEN, [2,3], 1, False))
        board.append(BuildingCard("farm", 1, CardType.BLUE, [2], 1, False))
        board.append(BuildingCard("wheat field", 1, CardType.BLUE, [1], 1, False))
        board.append(BuildingCard("cafe", 2, CardType.RED, [3], 1, False))
        board.append(BuildingCard("mini market", 2, CardType.GREEN, [4], 3, False))
        board.append(BuildingCard("forest", 3, CardType.BLUE, [5], 1, False))
        board.append(BuildingCard("mine", 6, CardType.BLUE, [9], 5, False))
        board.append(BuildingCard("milk factory", 5, CardType.GREEN, [7], 0, False))
        board.append(BuildingCard("furniture factory", 3, CardType.GREEN, [8], 0, False))
        board.append(BuildingCard("family restaurant", 3, CardType.RED, [9,10], 2, False))
        board.append(BuildingCard("mall", 2, CardType.GREEN, [11,12], 0, False))
        board.append(BuildingCard("plantation", 3, CardType.BLUE, [10], 3, False))
    
    for name in player_names:
        board.append(BuildingCard("stadium", 6, CardType.PURPLE, [6], 0, True))
        board.append(BuildingCard("television tower", 7, CardType.PURPLE, [6], 0, True))
        board.append(BuildingCard("office building", 8, CardType.PURPLE, [6], 0, True))

        player = Player(name)
        
        player.add_card(VictoryCard("train station", 4, CardType.GOLDEN, False))
        player.add_card(VictoryCard("shopping mall", 10, CardType.GOLDEN, False))
        player.add_card(VictoryCard("amusement park", 16, CardType.GOLDEN, False))
        player.add_card(VictoryCard("radio tower", 22, CardType.GOLDEN, False))
        
        player.buy_card(BuildingCard("bakery", 0, CardType.GREEN, [2,3], 1, False))
        player.buy_card(BuildingCard("wheat field", 0, CardType.BLUE, [1], 1, False))
        
        player.take_coins(3)
        
        players.append(player)
        
def play_game():
    play_round()
    
def play_round():
    for player in players:
        play_turn(player)
        
def play_turn(player):
    print "playing turn for " + player.name
    

def main():
    initialize_game()
    play_game()


if __name__ == "__main__":
    main()