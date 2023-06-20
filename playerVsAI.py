class Mancala_Board:
    def __init__(self, mancala):
        if mancala != None:
            self.mancala = mancala[:]
        else:
            self.mancala = [0 for i in range(14)]
            for i in range(0,6):
                self.mancala[i] = 4
            for i in range(7,13):
                self.mancala[i] = 4

    def player_move(self, i):
        j = i
        repeat_turn = False
        add = self.mancala[j]
        self.mancala[j] = 0
        if i > 6:
            stones = add
            while stones > 0:
                i += 1
                i = i % 14
                if i == 6:
                    continue
                else:
                    self.mancala[i % 14] += 1
                stones -= 1
            if i > 6 and self.mancala[i] == 1 and i != 13 and self.mancala[-i+12] != 0:
                self.mancala[13] += 1 + self.mancala[-i+12]
                self.mancala[i] = 0
                self.mancala[-i+12] = 0
            if i == 13:
                repeat_turn = True
        else:
            stones = add
            while (stones > 0):
                i += 1
                i = i % 14
                if i == 13:
                    continue
                else:
                    self.mancala[i%14] += 1
                stones -= 1
            if i < 6 and self.mancala[i] == 1 and i !=6 and self.mancala[-i + 12]!=0:
                self.mancala[6] += 1 + self.mancala[-i + 12]
                self.mancala[i] = 0
                self.mancala[-i + 12] = 0
            if i == 6:
                repeat_turn = True
        return repeat_turn

    def isEnd(self):
        if sum(self.mancala[0:6])==0 :
            self.mancala[13]+=sum(self.mancala[7:13])
            for i in range(14):
                if  (i != 13 and i != 6):
                    self.mancala[i] = 0

            return True
        elif sum(self.mancala[7:13])==0:
            self.mancala[6] += sum(self.mancala[0:6])
            for i in range(14):
                if  (i != 13 and i != 6):
                    self.mancala[i] = 0
            return True

        return False

    def print_mancala(self):
        for i in range(12,6,-1):
            print('  ', self.mancala[i], '   ', end = '')
        print('  ')
        print(self.mancala[13],'                                           ',self.mancala[6])

        for i in range(0,6,1):
            print('  ', self.mancala[i], '   ', end='')
        print('  ')
    def husVal(self):
        if self.isEnd():
            if self.mancala[13] > self.mancala[6]:
                return 100
            elif self.mancala[13] == self.mancala[6]:
                return 0
            else:
                 return -100
        else:
            return self.mancala[13] - self.mancala[6]
          
          
def alphabeta(mancala, depth, alpha, beta , MinorMax):
    if depth == 0 or mancala.isEnd():
        return mancala.husVal(), -1
    if MinorMax:
        v = -1000000
        player_move = -1
        for i in range(7, 13, 1):
            if mancala.mancala[i] == 0 : continue
            a = Mancala_Board(mancala.mancala[:])
            minormax = a.player_move(i)
            newv,_ = alphabeta(a, depth-1, alpha, beta, minormax)
            if v < newv:
                player_move = i
                v = newv
            alpha = max(alpha, v)
            if alpha >= beta :
                break
        return v, player_move
    else:
        v = 1000000
        player_move = -1
        for i in range(0, 6, 1):
            if mancala.mancala[i] == 0: continue
            a = Mancala_Board(mancala.mancala[:])
            minormax = a.player_move(i)
            newv,_ = alphabeta(a, depth - 1, alpha, beta, not minormax)
            if v > newv:
                player_move = i
                v = newv
            beta = min(beta, v)
            if alpha >= beta:
                break
        return v, player_move       
          
def player_aibot():
    j = Mancala_Board(None)
    j.print_mancala()
    while True:
        if j.isEnd():
            break
        while True:
            if j.isEnd():
                break
            h = int(input("YOUR TURN >>> "))
            if h > 5 or j.mancala[h] == 0:
                print("You can't Play at this position. Choose another position")
                continue
            t = j.player_move(h)
            j.print_mancala()
            if not t:
                break
        while True:
            if j.isEnd():
                break
            print("AI-BOT TURN >>> ", end = "")
            _,k = alphabeta(j, 10, -100000, 100000, True)
            print(k)
            t = j.player_move(k)
            j.print_mancala()
            if not t:
                break
    if j.mancala[6] < j.mancala[13]:
        print("AI-BOT WINS")
    else:
        print("YOU WIN")
    print('GAME ENDED')
    j.print_mancala()
                
print("\n:::: MANCALA BOARD GAME ::::")
print("!!! Welcome to Mancala Gameplay !!!")
while True:
    print("\nPlay the game")
    player_aibot()
    break