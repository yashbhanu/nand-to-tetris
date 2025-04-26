import os
from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable

filePath = input("Enter Hack Assembly File name eg.(abc.asm): ")

fileDirectory = os.path.dirname(filePath)
fileName = os.path.splitext(os.path.basename(filePath))[0]

result = ""
with open(filePath, "r") as f1:
    parser = Parser(f1)
    symbolTbl = SymbolTable()
    code = Code()

    lineCnt = -1

    while parser.hasMoreCommands():
        parser.advance()

        if parser.instructionType() == "L_INSTRUCTION":
            symbolTbl.addLabel(parser.symbol(), lineCnt+1)
        else:
            lineCnt+=1
        
    f1.seek(0)
    varAddress = 16

    while parser.hasMoreCommands():
        parser.advance()

        if parser.instructionType() == "A_INSTRUCTION":
            s = parser.symbol()
            c = ""
            if s.isnumeric():
                c = code.decToBin(parser.symbol())
            else:
                if symbolTbl.contains(s):
                    c = code.decToBin(symbolTbl.getAddress(parser.symbol()))
                else:
                    symbolTbl.addLabel(s,varAddress)
                    c = code.decToBin(varAddress)
                    varAddress += 1
            
            result += c + "\n"
        elif parser.instructionType() == "C_INSTRUCTION":
            dt = code.dest(parser.dest())
            cp = code.comp(parser.comp())
            jp = code.jump(parser.jump())

            result += "111" + cp + dt + jp + "\n"

with open(fileDirectory + "/" + fileName + ".hack", "w", newline="\n") as f2:
    f2.write(result[:-1])
