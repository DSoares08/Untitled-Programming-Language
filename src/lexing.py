class lineObject:
    def __init__(self, id):
        self.id = id

codeFile = open("code.txt")

for line in codeFile:
    line1 = lineObject(line.split()[0])

print(line1.id)