from card import Card, CardType
from player import Player

def main():
    
    player_names = ["Al", "So"]
    players = []
    board = []
    
    board.append(Card("bakery", 1, CardType.GREEN, [2,3], 1, False))
    board.append(Card("wheat field", 1, CardType.BLUE, [1], 1, False))
    board.append(Card("cafe", 2, CardType.RED, [3], 1, False))
    board.append(Card("train station", 4, CardType.GOLDEN, [], 0, True))
    
    for name in player_names:
    
        # initiate game
        bakery = Card("bakery", 0, CardType.GREEN, [2,3], 1, False)
        wheat_field = Card("wheat field", 0, CardType.BLUE, [1], 1, False)

        player = Player(name)
        player.take_coins(3)
        player.buy_card(bakery)
        player.buy_card(wheat_field)
        
        players.append(player)

if __name__ == "__main__":
    main()