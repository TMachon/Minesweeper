# coding: utf-8
import displayTerm
import random, re

# Made by Theo Machon

class Minesweeper:

    def __init__(self):

        ## Init atributes

        self.io = displayTerm.TerminalDisplayV2()

        self.recurStorage = []  # List: storage for "_discoverRecursive" function
        self.debug = False       # Bool: enable debug display

        self.diff = 0           # Int:  0:Novice, 1:Easy, 2:Medium, 3:Hard, 4:Impossible
        self.width = 0          # Int:  width of the file
        self.height = 0         # Int:  height of tje
        self.amtBombs = 0       # Int:  amont of bombs in the field
        self.running = True     # Bool: True while a game is running
        self.playing = True     # Bool: True while the player has not decided to stop playing

        self.amtDiscovered = 0  # Int:  amont of bombs discovered
        self.field = {}         # Dict: "field" as in minefield
            # (x, y, O): (int) bomb positions (maked as 9 or above) and case value (0-8)
            # (x, y, 1): (bool) discovered cases (True=discovered, False=hidden)

    def _setup(self):

        self.field = {}
        self.amtDiscovered = 0

        ## Set difficulty level

        self.diff = int(self.io.inputList("Select difficulty", ['Novice', 'Easy', 'Medium', 'Hard', 'Impossible']))

        ## Set dimensions

        self.width = int(self.io.inputInt("Select width (between 5 and 50)", 5, 50))
        self.height = int(self.io.inputInt("Select height (between 5 and 50)", 5, 50))

        ## Generate bombs

        if (self.diff == 0): self.amtBombs = int(self.width*self.height/6)
        elif (self.diff == 1): self.amtBombs = int(self.width*self.height/5)
        elif (self.diff == 2): self.amtBombs = int(self.width*self.height/3.2)
        elif (self.diff == 3): self.amtBombs = int(self.width*self.height/2.5)
        elif (self.diff == 4): self.amtBombs = int(self.width*self.height/2)

        self._fillFieldV1()
    
    def _fillFieldV1(self):

        bombsPos = random.sample(range(self.width*self.height), self.amtBombs)

        if (self.debug): print(bombsPos) #DEBUG

        ## Initialize tables and bombs

        for i in range(self.height):
            for j in range(self.width):
                if (j+i*self.width in bombsPos):
                    self.field[j, i, 0] = 9
                else:
                    self.field[j, i, 0] = 0
                self.field[j, i, 1] = False

        if (self.debug): self.io.displayDebug(self.field) #DEBUG

        # top left corner
        if (self.field[0, 0, 0] >=9):
            self.field[1, 0, 0] += 1
            self.field[0, 1, 0] += 1
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
            self.field[self.width-1, self.height-2, 0] += 1
            self.field[self.width-2, self.height-1, 0] += 1

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

        x = posX-1
        y = posY-1

        if (self.field[x, y, 1]):
            self.io.displayWarning("You chose an already defused spot, choose another one.")
        else:
            if (self.field[x, y, 0] >= 9):
                self.gameLost()
            else:
                self._discoverRecursive(x, y)
                self.recurStorage = []
                if ((self.amtBombs + self.amtDiscovered) >= (self.height * self.width)):
                    self.gameWon()

    def _discoverRecursive(self, x, y):

        self.amtDiscovered += 1
        self.field[x, y, 1] = True
        self.recurStorage.append((x,y))

        if (self.field[x, y, 0] == 0):

            top = (y > 0)
            left = (x > 0)
            right = (x < self.width-1)
            bottom = (y < self.height-1)

            # top left
            if (left and top and not (x-1,y-1) in self.recurStorage):
                self._discoverRecursive(x-1, y-1)

            # top
            if (top and not (x, y-1) in self.recurStorage):
                self._discoverRecursive(x, y-1)

            # top right
            if (right and top and not (x+1, y-1) in self.recurStorage):
                self._discoverRecursive(x+1, y-1)

            # right
            if (right and not (x+1, y) in self.recurStorage):
                self._discoverRecursive(x+1, y)

            # bottom right
            if (right and bottom and not (x+1, y+1) in self.recurStorage):
                self._discoverRecursive(x+1, y+1)

            # bottom
            if (bottom and not (x, y+1) in self.recurStorage):
                self._discoverRecursive(x, y+1)

            # bottom left
            if (left and bottom and not (x-1, y+1) in self.recurStorage):
                self._discoverRecursive(x-1, y+1)
            
            # left
            if (left and not (x-1, y) in self.recurStorage):
                self._discoverRecursive(x-1, y)

    def gameWon(self):
        self.io.displayGame(self.field)
        self.io.displayVictory()
        self.running = False

    def gameLost(self):
        self.io.displayDefeat()
        self.running = False

    def start(self):

        while (self.playing):

            self.running = True
            self._setup()

            if (self.debug): self.io.displayDebug(self.field) #DEBUG

            ## Main game loop
            while (self.running) :
                self.io.displayGame(self.field)
                (x,y) = self.io.getCoordinates(self.height, self.width)
                self.discover(x, y)
            
            self.playing = self.io.inputList("Do you want to play again ?", ["Yes", "No"]) == 0

        self.io.displayMessage("Thanks for playing, see you soon.")
                
Minesweeper().start()
