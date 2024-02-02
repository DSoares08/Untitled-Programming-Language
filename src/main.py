import lexing, parsing

program = '"hello"'
parser = parsing.Parser()
ast = parser.parse(program)
print(ast)
