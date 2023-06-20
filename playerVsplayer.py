class mancala_board:
    def __init__(self, mancala):
        if mancala != None:
            self.mancala = mancala[:]
        else:
            self.mancala = [0 for i in range(14)]
            for i in range(0,6):
                self.mancala[i] = 4    
            for i in range(7,13):
                self.mancala[i] = 4
                
print("\n:::: MANCALA BOARD GAME ::::")
print("!!! Welcome to Mancala Gameplay !!!")
while True:
    print("\nChoose your Gameplay Type")
    print("(1) Player-1 vs Player-2")
    print("(2) Player vs AI-Bot")
    type = int(input(">>> "))
    if type == 1:
        player_player()
        break
    elif type == 2:
        player_aibot()
        break
    else:
        print("Wrong Gameplay Type. Enter Again")
        continue