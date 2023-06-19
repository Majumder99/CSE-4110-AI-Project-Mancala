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
                