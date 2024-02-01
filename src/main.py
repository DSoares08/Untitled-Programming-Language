import lexing, parsing

codeFile = open("code.txt")

for line in codeFile:
    line = lexing.convertLineToList(line)
    parser = parsing.Parser()
    line = parser.parse(line)
    print(line)
