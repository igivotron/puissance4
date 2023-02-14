from board import P4

jeu = P4()
jeu.start()

loop = True
playerA = 1
playerB = -1
player = 1

print(jeu)
while loop:
    print("Player",player,"what's your next action ?")
    act = input("Action : ")
    if not jeu.slide(int(act),player):
        print(jeu)
    else:
        player *= -1
        print(jeu)
