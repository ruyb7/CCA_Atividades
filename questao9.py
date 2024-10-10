''' 
QUESTÃO 9

Construa um AFD em Python que reconheça strings contendo a sequência "101".

'''

class AFD:
    def __init__(self):
        self.states = {
            'q0': 0,
            'q1': 1,
            'q2': 2,
            'q3': 3
        }
        self.current_state = 'q0'

    def transition(self, input_symbol):
        if self.current_state == 'q0':
            if input_symbol == '1':
                self.current_state = 'q1'
            else:
                self.current_state = 'q0'
        elif self.current_state == 'q1':
            if input_symbol == '0':
                self.current_state = 'q2'
            else:
                self.current_state = 'q1'
        elif self.current_state == 'q2':
            if input_symbol == '1':
                self.current_state = 'q3'
            else:
                self.current_state = 'q0'
        elif self.current_state == 'q3':
            self.current_state = 'q3'

    def accepts(self, string):
        self.current_state = 'q0'
        for symbol in string:
            self.transition(symbol)
        return self.current_state == 'q3'

afd = AFD()
exemplos = ["001010", "1101", "101", "0101", "111", "000"]

for s in exemplos:
    if afd.accepts(s):
        print(f"A string '{s}' é aceita.")
    else:
        print(f"A string '{s}' não é aceita.")
