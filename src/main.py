import lexing

codeFile = open("code.txt")

for line in codeFile:
    line = lexing.convertLineToList(line)
    print(line)
