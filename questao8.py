''' 
QUESTÃO 8

Desenvolva um AFN que aceite strings onde o número de '0's é divisível por 3.

'''

class AFN:
    def __init__(self):
        self.states = {0, 1, 2}
        self.start_state = 0
        self.accept_states = {0}

    def transition(self, state, symbol):
        if symbol == '0':
            return (state + 1) % 3
        else:
            return state
    def accepts(self, input_string):
        current_state = self.start_state
        
        for symbol in input_string:
            current_state = self.transition(current_state, symbol)

        return current_state in self.accept_states

afn = AFN()

exemplos = ["", "1", "0", "00", "000", "0000", "00000", "0101010", "1111111", "000111"]
results = {s: afn.accepts(s) for s in exemplos}

for s, result in results.items():
    print(f"A string '{s}' é aceita? {result}")
