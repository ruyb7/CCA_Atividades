''' 
QUESTÃO 22

Desenvolva um AFD que reconheça uma linguagem onde a diferença entre o número de 'a's e 'b's
seja múltipla de 3.

'''

class AFD:
    def __init__(self):
        self.state = 0

    def transition(self, symbol):
        if self.state == 0:
            if symbol == 'a':
                self.state = 1
            elif symbol == 'b':
                self.state = 2
        elif self.state == 1:
            if symbol == 'a':
                self.state = 2
            elif symbol == 'b':
                self.state = 0
        elif self.state == 2:
            if symbol == 'a':
                self.state = 0
            elif symbol == 'b':
                self.state = 1

    def accepts(self, input_string):
        self.state = 0
        for symbol in input_string:
            self.transition(symbol)
        return self.state == 0

afd = AFD()

test_strings = [
    "aabb",
    "aaabbb",
    "aabbb",
    "aaabb",
    "aabab",
    "aaaabbbb"
]

for s in test_strings:
    result = afd.accepts(s)
    print(f"A string '{s}' é aceita? {result}")
