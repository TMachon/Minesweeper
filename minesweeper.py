# coding: utf-8
import displayTerm
import random, re

# Made by Theo Machon

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

    def _setup(self):

        ## Set difficulty level

        self.diff = int(self.display2.listInput("Select difficulty", ['Easy', 'Medium', 'Hard']))

        ## Set dimensions

        self.width = int(self.display2.intInput("Select width (between 5 and 50)", 5, 50))
        self.height = int(self.display2.intInput("Select height (between 5 and 50)", 5, 50))

        ## Generate bombs

        if (self.diff == 0): self.nbBombs = int(self.width*self.height/5)
        elif (self.diff == 1): self.nbBombs = int(self.width*self.height/3.2)
        elif (self.diff == 2): self.nbBombs = int(self.width*self.height/2.5)

        print(self.nbBombs) #DEBUG
   
        bombsPos = random.sample(range(self.width*self.height), self.nbBombs)

        print(bombsPos) #DEBUG

        ## Initialize tables and bombs

        for i in range(self.width):
            for j in range(self.height):
                if ((i*self.width)+j in bombsPos):
                    self.field[i, j, 0] = 9
                else:
                    self.field[i, j, 0] = 0
                self.field[i, j, 1] = False

        ## Place numbers

        # top left corner
        if (self.field[0, 0, 0] >=9):
            self.field[0, 1, 0] += 1
            self.field[1, 0, 0] += 1
            self.field[1, 1, 0] += 1

        # top right corner
        if (self.field[self.width-1, 0, 0] >= 9):
            self.field[self.width-2, 0, 0] += 1
            self.field[self.width-2, 1, 0] += 1
            self.field[self.width-1, 1, 0] += 1

        # bottom left corner
        if (self.field[0, self.height-1, 0] >= 9):
            self.field[0, self.height-2, 0] += 1
            self.field[1, self.height-2, 0] += 1
            self.field[1, self.height-1, 0] += 1

        # bottom right corner
        if (self.field[self.width-1, self.height-1, 0] >= 9):
            self.field[self.width-2, self.height-2, 0] += 1
            self.field[self.width-2, self.height-1, 0] += 1
            self.field[self.width-1, self.height-2, 0] += 1

        # top & bottom edges
        for i in range(1, self.width-1):
            if (self.field[i, 0, 0] >= 9):
                self.field[i-1, 0, 0] += 1
                self.field[i-1, 1, 0] += 1
                self.field[i, 1, 0] += 1
                self.field[i+1, 0, 0] += 1
                self.field[i+1, 1, 0] += 1

            if (self.field[i, self.height-1, 0] >= 9):
                self.field[i-1, self.height-2, 0] += 1
                self.field[i-1, self.height-1, 0] += 1
                self.field[i, self.height-2, 0] += 1
                self.field[i+1, self.height-2, 0] += 1
                self.field[i+1, self.height-1, 0] += 1
        
        # left & right edges
        for j in range(1, self.height-1):
            if (self.field[0, j, 0] >= 9):
                self.field[0, j-1, 0] += 1
                self.field[0, j+1, 0] += 1
                self.field[1, j-1, 0] += 1
                self.field[1, j, 0] += 1
                self.field[1, j+1, 0] += 1

            if (self.field[self.width-1, j, 0] >= 9):
                self.field[self.width-2, j-1, 0] += 1
                self.field[self.width-2, j, 0] += 1
                self.field[self.width-2, j+1, 0] += 1
                self.field[self.width-1, j-1, 0] += 1
                self.field[self.width-1, j+1, 0] += 1

        # middle
        for i in range(1, self.width-1):
            for j in range(1, self.height-1):
                if (self.field[i, j, 0] >= 9):
                    self.field[i-1, j-1, 0] += 1
                    self.field[i-1, j, 0] += 1
                    self.field[i-1, j+1, 0] += 1
                    self.field[i, j-1, 0] += 1
                    self.field[i, j+1, 0] += 1
                    self.field[i+1, j-1, 0] += 1
                    self.field[i+1, j, 0] += 1
                    self.field[i+1, j+1, 0] += 1
                    
    def discover(self, posX, posY):

        if (posX >= self.width or posX < 0):
            print("NO") #DEBUB
        if (posY >= self.height or posY < 0):
            print("NONO") #DEBUG

        if (self.field[posY-1, posY, 0] == 9):
            self.gameLost()
        else:
            self._discoverRecursive(posX, posX)

    def _discoverRecursive(self, posX, posY):

        posX -= 1
        posY -= 1

        if (posX >= 0 and posX < self.width and posY >= 0 and posY < self.width):
            self.field[posY, posX, 1] == True
            if (self.field[posY, posX, 0] == 0):
                self._discoverRecursive(posX-1, posY-1)
                self._discoverRecursive(posX-1, posY)
                self._discoverRecursive(posX-1, posY+1)
                self._discoverRecursive(posX, posY-1)
                self._discoverRecursive(posX, posY+1)
                self._discoverRecursive(posX+1, posY-1)
                self._discoverRecursive(posX+1, posY)
                self._discoverRecursive(posX+1, posY+1)

    def gameWon(self):
        self.display2.displayVictory()

    def gameLost(self):
        self.display2.displayDefeat()

    def start(self):

        self._setup()

        self.display2.debugDisplay(self.field) #Debug
                
        ## Main game loop
        while True :
            self.display2.gameDisplay(self.field)
            row = self.display2.intInput("Select a row for your next move", 1, self.height)
            column = self.display2.intInput("Select a column for your next move", 1, self.width)
            #self.discover(column, row)


Minesweeper().start()