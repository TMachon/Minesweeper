# coding: utf-8
import range_regex as rr
import termcolor as tc
import inquirer, re

# Made by Theo Machon

class TerminalDisplayV2:
    
    def gameDisplay(self, dictionary):

        width = max(list(dictionary.keys()))[0]+1
        height = max(list(dictionary.keys()))[1]+1

        splitLine = "  "
        for i in range(width):
            splitLine += "┼───"
        splitLine += "┤"

        endLine = "  "
        for i in range(width):
            endLine += "┴───"
        endLine += "┘"

        line = "   "
        for i in range(width):
            head = " "+str(i+1) if len(str(i+1))==1 else str(i+1)
            line += head+"  "
        
        print(line)

        for i in range(height):

            print(splitLine)

            head = " "+str(i+1) if len(str(i+1))==1 else str(i+1)
            line = head+"│"
            for j in range(width):
                #if (True): # DEBUG
                if (dictionary[j, i, 1]):
                    if (int(dictionary[j, i, 0]) == 0):
                        val = " "
                    elif (int(dictionary[j, i, 0]) == 1):
                        val = "\033[94m1\033[39m"
                    elif (int(dictionary[j, i, 0]) == 2):
                        val = "\033[92m2\033[39m"
                    elif (int(dictionary[j, i, 0]) == 3):
                        val = "\033[91m3\033[39m"
                    elif (int(dictionary[j, i, 0]) == 4):
                        val = "\033[95m4\033[39m"
                    elif (int(dictionary[j, i, 0]) == 5):
                        val = "\033[31m5\033[39m"
                    elif (int(dictionary[j, i, 0]) == 6):
                        val = "\033[96m6\033[39m"
                    elif (int(dictionary[j, i, 0]) == 7):
                        val = "\033[37m7\033[39m"
                    elif (int(dictionary[j, i, 0]) == 8):
                        val = "\033[90m8\033[39m"
                    elif (int(dictionary[j, i, 0]) >= 9):
                        val = "•"
                    else:
                        val = str(dictionary[j, i, 0])
                else:
                    val = "□"

                line += " "+val+" │"

            print(line)
        
        print(endLine)

    def debugDisplay(self, dictionary):

        width = max(list(dictionary.keys()))[0]+1
        height = max(list(dictionary.keys()))[1]+1

        for i in range(height):
            for j in range(width):
                print(str("{0:0=2d}".format(dictionary[j, i, 0]))+":"+str(dictionary[j, i, 1])[0]+" ", end='')
            print("")
        print("")

    def getCoordinates(self, height, width):

        row = self.intInput("Select a row for your next move", 1, height)
        column = self.intInput("Select a column for your next move", 1,  width)

        return((int(column), int(row)))

    def listInput(self, text, options):

        query = [inquirer.List('answer',
                message=text,
                choices=options
            ),]

        choice = inquirer.prompt(query)
        return options.index(choice.pop('answer'))
    
    def intInput(self, text, minimum, maximum):

        regex = rr.bounded_regex_for_range(minimum, maximum)

        query = [inquirer.Text('answer',
            message=text,
            validate=lambda _, x: re.match(regex, x)
        ),]

        choice = inquirer.prompt(query)
        return choice.pop('answer')

    def displayVictory(self):
        print("Congratulations, you won !")

    def displayDefeat(self):
        print("You loose, too bad!")

    def print(self, text):
        print(text)


    # Legacy code

    def input(self, message):
        return input(message)