''' 
QUESTÃO 12

Construa um AFD para uma linguagem sobre o alfabeto {a, b}, que reconheça strings com um
número ímpar de 'a's.


'''

class AFN:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.start_state = 'q0'
        self.accept_states = {'q3'}

    def transition(self, state, symbol):
        """Função de transição do AFN."""
        if state == 'q0':
            if symbol == '1':
                return {'q1'}
            elif symbol == '0':
                return {'q0'}

        elif state == 'q1':
            if symbol == '1':
                return {'q2'}
            elif symbol == '0':
                return {'q0'}

        elif state == 'q2':
            if symbol == '1':
                return {'q3'}
            elif symbol == '0':
                return {'q0'}

        elif state == 'q3':
            return {'q3'}

        return set()

    def accepts(self, string):
        current_states = {self.start_state}

        for symbol in string:
            next_states = set()
            for state in current_states:
                next_states.update(self.transition(state, symbol))
            current_states = next_states

        return not current_states.isdisjoint(self.accept_states)


afn = AFN()

test_strings = ["001", "110", "101010", "0110", "000", "111", "10011", "1100", "101"]
results = {s: afn.accepts(s) for s in test_strings}

for s, result in results.items():
    print(f"A string '{s}' é aceita? {result}")

