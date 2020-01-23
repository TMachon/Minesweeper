# coding: utf-8
import displayTerm
import random, re

class Minesweeper:

    def __init__(self):

        ## Init atributes
        self.display2 = displayTerm.TerminalDisplayV2()
        self.diff = 0   # 0: null, 1: easy, 2: medium, 3:hard
        self.width = 0
        self.height = 0
        self.nbBombs = 0
        self.nbDiscovered = 0

        self.field = {} # "field" as in minefield
        # (y, x, O): (int) bomb positions (maked as 9 or above) and case value (0-8)
        # (y, x, 1): (bool) discovered cases (True=discovered, False=hidden)

    def _settings(self):

        ## Set difficulty level
        while not (1<=self.diff<=3) :
            self.diff = int(self.display2.input("Select difficulty (1, 2, 3): "))

        ## Set dimensions
        while not (5<=self.height<=99) :
            self.height = int(self.display2.input("Select height (between 5 and 99): "))

        while not (5<=self.width<=99) :
            self.width = int(self.display2.input("Select width (between 5 and 99): "))

        ## Generate bombs
        if (self.diff == 1): self.nbBombs = int(self.width*self.height/5)
        elif (self.diff == 2): self.nbBombs = int(self.width*self.height/3.2)
        elif (self.diff == 3): self.nbBombs = int(self.width*self.height/2.5)

        print(self.nbBombs) #DEBUG
   
        bombsPos = random.sample(range(self.width*self.height), self.nbBombs)

        print(bombsPos) #DEBUG

        ## Initialize tables and bombs

        for i in range(self.height):
            for j in range(self.width):
                if ((i*self.width)+j in bombsPos):
                    self.field[i, j, 0] = 9
                else:
                    self.field[i, j, 0] = 0
                self.field[j, i, 1] = False

        ## Place numbers

        # top left corner
        if (self.field[0, 0, 0] >=9):
            self.field[0, 1, 0] += 1
            self.field[1, 0, 0] += 1
            self.field[1, 1, 0] += 1

        # top right corner
        if (self.field[0, self.width-1, 0] >= 9):
            self.field[0, self.width-2, 0] += 1
            self.field[1, self.width-2, 0] += 1
            self.field[1, self.width-1, 0] += 1

        # bottom left corner
        if (self.field[self.height-1, 0, 0] >= 9):
            self.field[self.height-2, 0, 0] += 1
            self.field[self.height-2, 1, 0] += 1
            self.field[self.height-1, 1, 0] += 1

        # bottom right corner
        if (self.field[self.height-1, self.width-1, 0] >= 9):
            self.field[self.height-2, self.width-2, 0] += 1
            self.field[self.height-2, self.width-1, 0] += 1
            self.field[self.height-1, self.width-2, 0] += 1


        # top & bottom edges
        for i in range(1, self.width-1):
            if (self.field[0, i, 0] >= 9):
                self.field[0, i-1, 0] += 1
                self.field[0, i+1, 0] += 1
                self.field[1, i-1, 0] += 1
                self.field[1, i, 0] += 1
                self.field[1, i+1, 0] += 1

            if (self.field[self.height-1, i, 0] >= 9):
                self.field[self.height-2, i-1, 0] += 1
                self.field[self.height-2, i, 0] += 1
                self.field[self.height-2, i+1, 0] += 1
                self.field[self.height-1, i-1, 0] += 1
                self.field[self.height-1, i+1, 0] += 1
        
        # left & right edges
        for i in range(1, self.height-1):
            if (self.field[i, 0, 0] >= 9):
                self.field[i-1, 0, 0] += 1
                self.field[i-1, 1, 0] += 1
                self.field[i, 1, 0] += 1
                self.field[i+1, 0, 0] += 1
                self.field[i+1, 1, 0] += 1

            if (self.field[i, self.width-1, 0] >= 9):
                self.field[i-1, self.width-2, 0] += 1
                self.field[i-1, self.width-1, 0] += 1
                self.field[i, self.width-2, 0] += 1
                self.field[i+1, self.width-2, 0] += 1
                self.field[i+1, self.width-1, 0] += 1

        # middle
        for i in range(1, self.height-1):
            for j in range(1, self.width-1):
                if (self.field[i, j, 0] >= 9):
                    self.field[i-1, j-1, 0] += 1
                    self.field[i-1, j, 0] += 1
                    self.field[i-1, j+1, 0] += 1
                    self.field[i, j-1, 0] += 1
                    self.field[i, j+1, 0] += 1
                    self.field[i+1, j-1, 0] += 1
                    self.field[i+1, j, 0] += 1
                    self.field[i+1, j+1, 0] += 1
                    
    def discover(self, pos):
        tmp = pos.split(':')
        x = int(tmp[0])-1
        y = int(tmp[1])-1

        if (x >= self.width or x < 0):
            print("NO")
        if (y >= self.height or y < 0):
            print("NONO")

        if (self.field[y-1, x, 0] == 9):
            self.gameLost()
        else:
            self._discoverRecursive(x, y)

    def _discoverRecursive(self, x, y):
        x -= 1
        y -= 1
        if (x >= 0 and x < self.width and y >= 0 and y < self.width):
            self.field[y, x, 1] == True
            if (self.field[y, x, 0] == 0):
                self._discoverRecursive(x-1, y-1)
                self._discoverRecursive(x-1, y)
                self._discoverRecursive(x-1, y+1)
                self._discoverRecursive(x, y-1)
                self._discoverRecursive(x, y+1)
                self._discoverRecursive(x+1, y-1)
                self._discoverRecursive(x+1, y)
                self._discoverRecursive(x+1, y+1)

    def gameWon(self):
        print("Congratulations, you won !")

    def gameLost(self):
        print("You loose, too bad!")

    def start(self):

        self._settings()

        self.display2.debugDisplay(self.field) #Debug
                
        ## Main game loop
        while True :
            self.display2.gameDisplay(self.field)
            val = ""
            while not (re.match("^[0-9]{1,2}:[0-9]{1,2}$", val)) :
                val = self.display2.input("Type in the case (X:Y) that you want to discover: ")

Minesweeper().start()