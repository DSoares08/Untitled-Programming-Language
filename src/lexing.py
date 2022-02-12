id = ["OUTPUT", "INPUT", "FOR", "WHILE", "IF", "ELSE", "ELIF"]
operation = ["+","-","*","/","==","<>","<",">","%","^","="]

def checkDataType(var):
    if var in id:
        return var + ": ID"
    elif var.isnumeric():
        return var + ": INT"
    elif var.isalpha():
        return var + ": VAR"
    elif var in operation:
        return var + ": OP"

def convertLineToList(line):
    #Declare variables
    splitedLine = []
    text = ""
    letterFlag = False
    counter = 0

    #Read line character per character
    for c in line:
        counter += 1
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
                splitedLine.append(checkDataType(text))
            text = ""
        elif c in " " and letterFlag:
            text += c
        elif c in '"':
            if text != "" or text:
                splitedLine.append(checkDataType(text))
            text = ""
            letterFlag = True

        if counter == len(line):
            if text[len(text)-1:] == "\n":
                text = text[:-1]
            if text != "" or text:
                splitedLine.append(checkDataType(text))

    #Return the line in a list
    return splitedLine
