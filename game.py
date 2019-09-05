import displayTerm
import random

class Minesweeper:

    def __init__(self):

        ## Init atributes
        self.display = displayTerm.TerminalDisplay()
        self.diff = 0   #0: null, 1: easy, 2: medium, 3:hard
        self.width = 0
        self.height = 0
        self.nbBombs = 0
        self.bombTable = [] #int 2D table with bomb postions (maked as 9) and case value (0-8)
        self.viewTable = [] #bool 2D table with discovered cases
        

    def __settings(self):

        ## Set difficulty level
        while not (1<=self.diff<=3) :
            self.diff = int(self.display.input("Select difficulty (1, 2, 3): "))

        ## Set dimensions
        while not (5<=self.width<=99) :
            self.width = int(self.display.input("Select width (between 5 and 99): "))

        while not (5<=self.height<=99) :
            self.height = int(self.display.input("Select height (between 5 and 99): "))

        ## Generate bombs
        if (self.diff == 1): self.nbBombs = int(self.width*self.height/5)
        elif (self.diff == 2): self.nbBombs = int(self.width*self.height/3.2)
        elif (self.diff == 3): self.nbBombs = int(self.width*self.height/2.5)
        print(self.nbBombs)
   
        bombsPos = random.sample(range(self.width*self.height), self.nbBombs)
        print(bombsPos)

        ## Set tables

        #TODO gere les bords
        for i in range(self.height):
            bombLine = []
            viewLine = []
            for j in range(self.width):
                if ((i*self.width)+j in bombsPos):
                    bombLine.append(9)
                else:
                    bombLine.append(0)
                viewLine.append(True)
            self.bombTable.append(bombLine)
            self.viewTable.append(viewLine)

        for i in range(self.height):
            for j in range(self.width):
                if (self.bombTable[i][j] >= 9):
                    try:
                        self.bombTable[i-1][j-1] +=1
                        self.bombTable[i-1][j] +=1
                        self.bombTable[i-1][j+1] +=1
                        self.bombTable[i][j-1] +=1
                        self.bombTable[i][j+1] +=1
                        self.bombTable[i+1][j-1] +=1
                        self.bombTable[i+1][j] +=1
                        self.bombTable[i+1][j+1] +=1
                    except:
                        print("err lol")


    def __start(self):
        self.display.output(self.bombTable, self.viewTable)

    def game(self):
        self.__settings()
        self.__start()