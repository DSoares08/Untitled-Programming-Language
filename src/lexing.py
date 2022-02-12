id = ["OUTPUT", "INPUT", "FOR", "WHILE", "IF", "ELSE", "ELIF", "TO", "RANGE", "NEXT", "ENDIF", "ENDWHILE", "FUNCTION", "PROCEDURE"]
operation = ["+","-","*","/","==","<>","<",">","%","^","=","<=",">=", "<-"]

def checkDataType(var):
    if var in id:
        return var + ": ID"
    elif var.isnumeric():
        return var + ": INT"
    elif var.isalpha():
        return var + ": VAR"
    elif var in operation:
        return var + ": OP"

    for op in operation:
        if op in var:
            print("Operation")

    return var + ": NO DATA TYPE FOUND"

def convertLineToList(line):
    #Declare variables
    splitedLine = []
    text = ""
    letterFlag = False
    counter = 0

    #Read line character per character
    for c in line:

        if c not in '" ' and not letterFlag:
            text += c
        elif c in '"' and letterFlag:
            if text != "":
                splitedLine.append(text+": STR")
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

        #Removes the back to the line for the last item in the list
        counter += 1
        if counter == len(line):
            if text[len(text)-1:] == "\n":
                text = text[:-1]
            if text != "" or text:
                splitedLine.append(checkDataType(text))

    #Return the line in a list
    return splitedLine

#IMPORTANT LEXING CANNOT RECOGNISE THE FACT THAT THIS var==0 is three different items however it works if written like this var == 0 !! NEEDS TO BE FIXED
