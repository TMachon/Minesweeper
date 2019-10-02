# coding: utf-8
import displayTerm
import random, re

class Minesweeper:

    def __init__(self):

        ## Init atributes
        self.display = displayTerm.TerminalDisplay()
        self.diff = 0   #0: null, 1: easy, 2: medium, 3:hard
        self.width = 0
        self.height = 0
        self.nbBombs = 0
        self.nbDiscovered = 0
        self.bombTable = [] #int 2D table with bomb postions (maked as 9) and case value (0-8)
        self.viewTable = [] #bool 2D table with discovered cases (True=discovered, False=hidden)

    def _settings(self):

        ## Set difficulty level
        while not (1<=self.diff<=3) :
            self.diff = int(self.display.input("Select difficulty (1, 2, 3): "))

        ## Set dimensions
        while not (5<=self.height<=99) :
            self.height = int(self.display.input("Select height (between 5 and 99): "))

        while not (5<=self.width<=99) :
            self.width = int(self.display.input("Select width (between 5 and 99): "))

        ## Generate bombs
        if (self.diff == 1): self.nbBombs = int(self.width*self.height/5)
        elif (self.diff == 2): self.nbBombs = int(self.width*self.height/3.2)
        elif (self.diff == 3): self.nbBombs = int(self.width*self.height/2.5)
        print(self.nbBombs)
   
        bombsPos = random.sample(range(self.width*self.height), self.nbBombs)
        print(bombsPos)

        ## Initialize tables and bombs

        for i in range(self.height):
            bombLine = []
            viewLine = []
            for j in range(self.width):
                if ((i*self.width)+j in bombsPos):
                    bombLine.append(9)
                else:
                    bombLine.append(0)
                viewLine.append(False)
            self.bombTable.append(bombLine)
            self.viewTable.append(viewLine)

        ## Place numbers

        #corners
        if (self.bombTable[0][0] >=9):
            self.bombTable[0][1] += 1
            self.bombTable[1][0] += 1
            self.bombTable[1][1] += 1
        if (self.bombTable[0][self.width-1] >= 9):
            self.bombTable[0][self.width-2] += 1
            self.bombTable[1][self.width-2] += 1
            self.bombTable[1][self.width-1] += 1
        if (self.bombTable[self.height-1][0] >= 9):
            self.bombTable[self.height-2][0] += 1
            self.bombTable[self.height-2][1] += 1
            self.bombTable[self.height-1][1] += 1
        if (self.bombTable[self.height-1][self.width-1] >= 9):
            self.bombTable[self.height-2][self.width-2] += 1
            self.bombTable[self.height-2][self.width-1] += 1
            self.bombTable[self.height-1][self.width-2] += 1

        #edges
        for i in range(1, self.width-1):
            if (self.bombTable[0][i] >= 9):
                self.bombTable[0][i-1] += 1
                self.bombTable[0][i+1] += 1
                self.bombTable[1][i-1] += 1
                self.bombTable[1][i] += 1
                self.bombTable[1][i+1] += 1
            if (self.bombTable[self.height-1][i] >= 9):
                self.bombTable[self.height-2][i-1] += 1
                self.bombTable[self.height-2][i] += 1
                self.bombTable[self.height-2][i+1] += 1
                self.bombTable[self.height-1][i-1] += 1
                self.bombTable[self.height-1][i+1] += 1
        
        for i in range(1, self.height-1):
            if (self.bombTable[i][0] >= 9):
                self.bombTable[i-1][0] += 1
                self.bombTable[i-1][1] += 1
                self.bombTable[i][1] += 1
                self.bombTable[i+1][0] += 1
                self.bombTable[i+1][1] += 1
            if (self.bombTable[i][self.width-1] >= 9):
                self.bombTable[i-1][self.width-2] += 1
                self.bombTable[i-1][self.width-1] += 1
                self.bombTable[i][self.width-2] += 1
                self.bombTable[i+1][self.width-2] += 1
                self.bombTable[i+1][self.width-1] += 1

        #center
        for i in range(1, self.height-1):
            for j in range(1, self.width-1):
                if (self.bombTable[i][j] >= 9):
                    self.bombTable[i-1][j-1] += 1
                    self.bombTable[i-1][j] += 1
                    self.bombTable[i-1][j+1] += 1
                    self.bombTable[i][j-1] += 1
                    self.bombTable[i][j+1] += 1
                    self.bombTable[i+1][j-1] += 1
                    self.bombTable[i+1][j] += 1
                    self.bombTable[i+1][j+1] += 1

    def discover(self, pos):
        tmp = pos.split(':')
        x = int(tmp[0])-1
        y = int(tmp[1])-1

        if (x >= self.width or x < 0):
            print("NO")
        if (y >= self.height or y < 0):
            print("NONO")

        if (self.bombTable[y-1][x] == 9):
            self.gameLost()
        else:
            self._discoverRecursive(x, y)

    def _discoverRecursive(self, x, y):
        # Reminder:
        #  self.bombTable = [] #int 2D table with bomb postions (maked as 9) and case value (0-8)
        #  self.viewTable = [] #bool 2D table with discovered cases
        if (x >= 0 and x < self.width and y >= 0 and y < self.width):
            if not (self.viewTable[y][x]):
                self.viewTable[y][x] == True
                if (self.bombTable[y][x] == 0):
                    self._discoverRecursive(x-1, y-1)
                    self._discoverRecursive(x-1, y)
                    self._discoverRecursive(x-1, y+1)
                    self._discoverRecursive(x, y-1)
                    self._discoverRecursive(x, y+1)
                    self._discoverRecursive(x+1, y-1)
                    self._discoverRecursive(x+1, y)
                    self._discoverRecursive(x+1, y+1)
                    #TODO FIX

    def gameWon(self):
        print("Congratulations, you won !")

    def gameLost(self):
        print("You loose, too bad!")

    def start(self):

        self._settings()

        self.display.output(self.bombTable, self.viewTable)

        val = ""
        while not (re.match("^[0-9]{1,2}:[0-9]{1,2}$", val)) :
            val = self.display.input("Type in the case (X:Y) that you want to discover: ")
        self.discover(val)

        self.display.output(self.bombTable, self.viewTable)

game = Minesweeper()
game.start()