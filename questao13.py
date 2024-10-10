''' 
QUESTÃO 13

Desenvolva um AFD que reconheça strings binárias onde o número de '1's seja maior que o número
de '0's.

'''

class AFD:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.start_state = 'q0'
        self.accept_states = {'q1'}

    def transition(self, state, symbol):
        """Função de transição do AFD."""
        if state == 'q0':
            if symbol == '1':
                return 'q1'
            elif symbol == '0':
                return 'q2'
        elif state == 'q1':
            if symbol == '1':
                return 'q1'
            elif symbol == '0':
                return 'q1'
        elif state == 'q2':
            if symbol == '1':
                return 'q2'
            elif symbol == '0':
                return 'q2'

        return None

    def accepts(self, string):
        """Verifica se a string é aceita pelo AFD."""
        current_state = self.start_state

        for symbol in string:
            current_state = self.transition(current_state, symbol)
            if current_state is None:
                return False

        return current_state in self.accept_states


afd = AFD()

test_strings = ["1", "0", "11", "00", "101", "1001", "1110", "000", "111"]
results = {s: afd.accepts(s) for s in test_strings}

for s, result in results.items():
    print(f"A string '{s}' é aceita? {result}")
