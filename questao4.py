''' 
QUESTÃO 4

Desenvolva um AFD que aceite strings com pelo menos um '0'.

'''
class AFD:
    def __init__(self):
        self.states = ['q0', 'q1']
        self.initial_state = 'q0'
        self.final_states = ['q1']
        self.current_state = self.initial_state

        self.transitions = {
            ('q0', '0'): 'q1',
            ('q0', '1'): 'q0',
            ('q1', '0'): 'q1',
            ('q1', '1'): 'q1'
        }

    def transition(self, symbol):
        self.current_state = self.transitions.get((self.current_state, symbol), self.current_state)

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