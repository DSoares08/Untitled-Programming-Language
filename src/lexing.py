id = ["OUTPUT", "INPUT", "FOR", "WHILE"]

class lineObject:
    def __init__(self, id):
        self.id = id

codeFile = open("code.txt")

for line in codeFile:
    if line[-1] != " ":
        line += "  "
    splitedLine = []
    text = ""
    letterFlag = False
    for c in line:
        if c not in '" ' and not letterFlag:
            text += c
        elif c in '"' and letterFlag:
            if text != "":
                splitedLine.append(text+": STRING")
            text = ""
            letterFlag = False
        elif c not in '" ' and letterFlag:
            text += c
        elif c in " " and not letterFlag:
            if text != "":
                splitedLine.append(text)
            text = ""
        elif c in " " and letterFlag:
            text += c
        elif c in '"':
            if text != "" or text:
                splitedLine.append(text)
            text = ""
            letterFlag = True
        
    if len(splitedLine) > 0:
        if splitedLine[-1] == "\n":
            splitedLine.pop(-1)
        elif splitedLine[-1][len(splitedLine[-1])-1:] == "\n":
            text2 = splitedLine[-1][:-1]
            splitedLine.pop(-1)
            splitedLine.append(text2)

    print(splitedLine)
