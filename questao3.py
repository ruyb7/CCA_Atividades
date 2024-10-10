''' 
QUESTÃO 3

Construa um AFD que reconheça a linguagem de strings que contenham exatamente dois '1's sobre o
alfabeto {0, 1}

'''

class AFD:
    def __init__(self):
        self.states = ['q0', 'q1', 'q2', 'q3']
        self.initial_state = 'q0'
        self.final_states = ['q2']
        self.current_state = self.initial_state
        self.transitions = {
            ('q0', '0'): 'q0',
            ('q0', '1'): 'q1',
            ('q1', '0'): 'q1',
            ('q1', '1'): 'q2',
            ('q2', '0'): 'q2',
            ('q2', '1'): 'q3',
            ('q3', '0'): 'q3',
            ('q3', '1'): 'q3'
        }

    def transition(self, symbol):
        self.current_state = self.transitions.get((self.current_state, symbol), 'q3')

    def accepts(self, string):
        self.current_state = self.initial_state
        for symbol in string:
            if symbol not in ['0', '1']:
                raise ValueError("A string deve conter apenas os símbolos '0' e '1'.")
            self.transition(symbol)
        return self.current_state in self.final_states

afd = AFD()

strings = ["", "0", "1", "10", "11", "0011", "000", "101010", "10001", "111"]
for string in strings:
    print(f"'{string}': {'Aceita' if afd.accepts(string) else 'Rejeitada'}")