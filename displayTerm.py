# coding: utf-8

class TerminalDisplay:
    
    def output(self, tableForBombs, tableForClicks):

        height = len(tableForBombs)
        width = len(tableForBombs[0])

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
                #if (tableForClicks[j][i]):
                if (True):
                    val = "•" if tableForBombs[j][i]>=9 else str(tableForBombs[j][i])
                else:
                    val = "□"
                #val=str(tableForClicks[j][i])[0]
                line += " "+val+" │"
                print

            print(line)
        
        print(endLine)

    def input(self, message):
        return input(message)

class TerminalDisplayV2:
    
    def gameDisplay(self, dictionary):

        height = max(list(dictionary.keys()))[0]+1
        width = max(list(dictionary.keys()))[1]+1

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
                if (dictionary[j, i, 1]):
                    val = "•" if dictionary[j, i, 0]>=9 else str(dictionary[j, i, 0])
                else:
                    val = "□"

                line += " "+val+" │"
                print

            print(line)
        
        print(endLine)

    def debugDisplay(self, dictionary):

        height = max(list(dictionary.keys()))[0]+1
        width = max(list(dictionary.keys()))[1]+1

        for j in range(height):
            for i in range(width):
                print(str("{0:0=2d}".format(dictionary[j, i, 0]))+":"+str(dictionary[j, i, 1])[0]+" ", end='')
            print("")

    def input(self, message):
        return input(message)