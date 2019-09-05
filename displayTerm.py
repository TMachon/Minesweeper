class TerminalDisplay:
    
    def output(self, tableForBombs, tableForClicsk):

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
                val = "•" if tableForBombs[j][i]>=9 else str(tableForBombs[j][i])
                line += " "+val+" │"

            print(line)
        
        print(endLine)

    def input(self, message: str) -> str:
        return input(message)