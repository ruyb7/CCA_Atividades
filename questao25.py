''' 
QUESTÃO 25

Implemente um AFD que aceite strings sobre {0, 1} onde a sequência "010" aparece pelo menos
duas vezes.

'''

class AFD:
    def __init__(self):
        self.state = 0

    def transition(self, symbol):
        if self.state == 0:
            if symbol == '0':
                self.state = 1
            else:
                self.state = 0
        elif self.state == 1:
            if symbol == '1':
                self.state = 2
            else:
                self.state = 0
        elif self.state == 2:
            if symbol == '0':
                self.state = 3
            else:
                self.state = 0
        elif self.state == 3:
            if symbol == '0':
                self.state = 1
            elif symbol == '1':
                self.state = 4
        elif self.state == 4:
            if symbol == '0':
                self.state = 1
            else:
                self.state = 4

    def accepts(self, input_string):
        self.state = 0
        for symbol in input_string:
            self.transition(symbol)
        return self.state == 4

afd = AFD()

test_strings = [
    "0101010",
    "01010",
    "0010010",
    "0100010",
    "1110110",
    "0000",
    "101010",
    "111001010",
    "010010010" 
]

for s in test_strings:
    result = afd.accepts(s)
    print(f"A string '{s}' é aceita? {result}")

