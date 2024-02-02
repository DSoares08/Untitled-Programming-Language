import lexing2

class Parser:
    def __init__(self):
        self._lexer = lexing2.Lexer()
        self._string = '' 

    def parse(self, string):
        self._string = string
        self._lexer.init(string)
        self._lookahead = self._lexer.getNextToken()
        return self.program()

    def program(self):
        return {type: 'program', 'body': self.Literal()}

    def expressionStatement(self):
        expression = self.Expression()
        self._eat(';')
        return {'type': 'ExpressionStatement', expression}

    def Expression(self):
        return self.AdditiveExpression()

    def AdditiveExpression(self):
        return self._BinaryExpression('MultiplicativeExpression', 'ADDITIVE_OPERATOR')

    def MultiplicativeExpression(self):
        return self._BinaryExpression('PrimaryExpression', 'MULTIPLICATIVE_OPERATOR')

    def _BinaryExpression(builderName, operatorToken):
        left = self.[builderName]()
        while type[self._lookahead] == operatorToken:
            operator = value[self._eat(operatorToken)
            right = self.[builderName]()
            left = {'type': 'BinaryExpression', operator, left, right}
        return left

    def PrimaryExpression(self):
        if type[self._lookahead] == '(':
            return self.ParenthesizedExpression()
        else:
            return self.Literal()

    def ParenthesizedExpression(self):
        self._eat('(')
        expression = self.Expression()
        self._eat(')')
        return expression

    def Literal(self):
        if type[self._lookahead] == 'NUMBER':
            return self.NumericLiteral()
        elif type[self._lookahead] == 'STRING':
            return self.StringLiteral()
        raise SyntaxError('Literal: unexpected literal production')

    def stringLiteral(self):
        token = self._eat('STRING')
        return {'type': 'str', 'value': token['value'[1:-1]]}

    def numericLiteral(self):
        token = self._eat('NUMBER')
        return {type: 'int', 'value': int(token['value'])}

    def _eat(tokenType):
        token = self._lookahead

        if token == None:
            raise SyntaxError(f'Unexpected end of input, expected: "{tokenType}"')

        if token[type] != tokenType:
            raise SyntaxError(f'Unexpected token: "{token[value]}", expected: "{tokenType}"')

        self._lookahead = self._lexer.getNextToken()
        return token
            

