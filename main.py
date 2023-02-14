from rules import P4
from board import Board

game = P4()
game.start()



playerA = 1
playerB = -1
player = 1

print(game)

### Set False if you don't want an interface ###
interface = False
if interface:
    board = Board()
    board.setup() 

while game.loop:
    print("Player",player,"what's your next action ?")
    act = input("Action : ")
    if not game.slide(int(act),player):
        print(game)
    else:
        player *= -1
        print(game)
        if interface:
            board.draw(game.matrix)
