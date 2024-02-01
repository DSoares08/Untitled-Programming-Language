class Parser:
    def parse(token_list):
        self._token_list = token_list

    def program():
        return {type: 'program', body: self.numericLiteral()}

    def numericLiteral():
        return {type: 'int', value: int(self._token_list)}

