class Parser:
    def __init__(self, fileStream):
        self.fileStream = fileStream
        self.currentInstruction = None

    def hasMoreCommands(self):
        pos = self.fileStream.tell()
        t = bool(self.fileStream.readline())
        self.fileStream.seek(pos)
        return t
    
    def advance(self):
        while True:
            t = self.fileStream.readline()
            t = t.partition("//")[0] #removing comments
            t = t.replace("\n","") #removing next lines
            t = t.replace(" ","") #removing spaces

            if t:
                break

        self.currentInstruction = t

    def instructionType(self):
        if self.currentInstruction[0] == "@":
            return "A_INSTRUCTION"
        elif self.currentInstruction[0] == "(":
            return "L_INSTRUCTION"
        else:
            return "C_INSTRUCTION"

    def symbol(self):
        if self.currentInstruction[0] == "@":
            return self.currentInstruction[1:]
        elif self.currentInstruction[0] == "(":
            return self.currentInstruction[1:-1]

    def dest(self):
        t1 = self.currentInstruction.find("=")
        return self.currentInstruction[:t1] if t1!=-1 else None
    
    def comp(self):
        t1 = self.currentInstruction.find("=")
        t2 = self.currentInstruction.find(";")
        return self.currentInstruction[t1+1 if t1!=-1 else 0 : t2 if t2!=-1 else None]
    
    def jump(self):
        t2 = self.currentInstruction.find(";")
        return self.currentInstruction[t2+1:] if t2!=-1 else None