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
                if (tableForClicks[j][i]):
                    val = "•" if tableForBombs[j][i]>=9 else str(tableForBombs[j][i])
                else:
                    val = "□"
                line += " "+val+" │"

            print(line)
        
        print(endLine)



    def input(self, message):
        return input(message)