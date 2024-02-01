id = ["OUTPUT", "INPUT", "FOR", "WHILE", "IF", "ELSE", "ELIF", "TO", "RANGE", "NEXT", "ENDIF", "ENDWHILE", "FUNCTION", "PROCEDURE","INTEGER", "STRING", "DECLARE", "AND", "OR", "NOT", "THEN"]
operation = ["+","-","*","/","==","<>","<",">","%","^","=","<=",">=", "<-",":"]

def checkDataType(var):
    if var in id:
        return var + ": ID"
    elif var.isnumeric():
        return var + ": INT"
    elif var in operation:
        return var + ": OP"
    elif not var.isnumeric():
        return var + ": VAR"


def convertLineToList(line):
    #Declare variables
    splitedLine = []
    text = ""
    letterFlag = False
    operationFlag = False
    counter = 0

    #Read line character per character
    for c in line:

        if c not in '" ' and not letterFlag:
            if c in operation:
                if operationFlag:
                    text += c
                elif text != "":
                    splitedLine.append(checkDataType(text))
                    operationFlag = True
                    text = c
                else:
                    operationFlag = True
                    text = c
            elif operationFlag:
                splitedLine.append(text+": OP")
                text = c
                operationFlag = False
            else:
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
            if operationFlag:
                operationFlag = False
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


