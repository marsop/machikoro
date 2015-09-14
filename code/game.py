from card import Card, BuildingCard, VictoryCard, CardType
from player import Player

def main():
    
    player_names = ["Al", "So"]
    players = []
    board = []
    
    board.append(BuildingCard("bakery", 1, CardType.GREEN, [2,3], 1, False))
    board.append(BuildingCard("wheat field", 1, CardType.BLUE, [1], 1, False))
    board.append(BuildingCard("cafe", 2, CardType.RED, [3], 1, False))
    board.append(VictoryCard("train station", 4, CardType.GOLDEN, False))
    board.append(VictoryCard("amusement park", 10, CardType.GOLDEN, False))
    board.append(VictoryCard("card3", 16, CardType.GOLDEN, False))
    board.append(VictoryCard("card4", 22, CardType.GOLDEN, False))
    
    for name in player_names:
    
        # initiate game
        bakery = BuildingCard("bakery", 0, CardType.GREEN, [2,3], 1, False)
        wheat_field = BuildingCard("wheat field", 0, CardType.BLUE, [1], 1, False)

        player = Player(name)
        player.take_coins(3)
        player.buy_card(bakery)
        player.buy_card(wheat_field)
        
        players.append(player)

if __name__ == "__main__":
    main()