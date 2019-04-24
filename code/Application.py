from game import Game

def main():

    for i in range(1,10):
        game = Game(False)
        game.initialize_game()
        winner = game.play_game()
        print('{}:{}'.format(i, winner.name))

if __name__ == "__main__":
    main()
