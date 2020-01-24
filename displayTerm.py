# coding: utf-8
import range_regex as rr
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

        for j in range(height):

            print(splitLine)

            head = " "+str(j+1) if len(str(j+1))==1 else str(j+1)
            line = head+"│"
            for i in range(width):
                if (dictionary[i, j, 1]):
                    val = "•" if int(dictionary[i, j, 0])>=9 else str(dictionary[i, j, 0])
                else:
                    val = "□"

                line += " "+val+" │"

            print(line)
        
        print(endLine)

    def debugDisplay(self, dictionary):

        height = max(list(dictionary.keys()))[0]+1
        width = max(list(dictionary.keys()))[1]+1

        for j in range(height):
            for i in range(width):
                print(str("{0:0=2d}".format(dictionary[j, i, 0]))+":"+str(dictionary[j, i, 1])[0]+" ", end='')
            print("")

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