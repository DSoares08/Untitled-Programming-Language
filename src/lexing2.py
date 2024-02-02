class Lexer:
    def __init__(self):
        self._string = ''
        self._cursor = 0

    def isEOF(self):
        return self._cursor == len(self._string)

    def init(self, string):
        self._string = string

    def hasMoreTokens(self):
        return self._cursor < len(self._string) 

    def getNextToken(self):
        if not self.hasMoreTokens():
            return None

        string = self._string[self._cursor:]

        if string[0].isdigit():
            number = ''
            while string[self._cursor].isdigit(): 
                number += string[self._cursor]
                self._cursor += 1
            return {'type': 'NUMBER', 'value': number}

        if string[0] == '"':
            s = ''
            self._cursor += 1
            s += string[self._cursor]
            while string[self._cursor] != '"' and not self.isEOF():
                self._cursor += 1
                s += string[self._cursor]
            self._cursor += 1
            s += string[self._cursor]
            return {'type': 'STRING', 'value': s}
        elif string[0] == "'":
            s = ''
            self._cursor += 1
            s += string[self._cursor]
            while string[self._cursor] != "'" and not self.isEOF():
                self._cursor += 1
                s += string[self._cursor]
            self._cursor += 1
            s += string[self._cursor]
            return {'type': 'STRING', 'value': s}
        return None

