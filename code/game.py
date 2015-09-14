from card import Card, CardType
from player import Player

def main():
    
    player_names = ["Al", "So"]
    players = []
    
    for name in player_names:
    
        # initiate game
        bakery = Card("bakery", 0, CardType.GREEN)
        wheat_field = Card("wheat field", 0, CardType.BLUE)

        player = Player(name)
        player.take_card(bakery)
        player.take_card(wheat_field)
        
        players.append(player)

if __name__ == "__main__":
    main()