''' 
QUESTÃO 10

Implemente um AFN que aceite qualquer string que tenha pelo menos um '0' seguido de pelo
menos um '1'.

'''

class AFN:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.start_state = 'q0'
        self.accept_states = {'q2'}

    def transition(self, state, symbol):
        if state == 'q0':
            if symbol == '0':
                return {'q1'}
            else:
                return set()

        elif state == 'q1':
            if symbol == '0':
                return {'q1'}
            elif symbol == '1':
                return {'q2'}
            else:
                return set()

        elif state == 'q2':
            return {'q2'}

        return set()

    def accepts(self, string):
        """Verifica se a string é aceita pelo AFN."""
        current_states = {self.start_state}

        for symbol in string:
            next_states = set()
            for state in current_states:
                next_states.update(self.transition(state, symbol))
            current_states = next_states

        return not current_states.isdisjoint(self.accept_states)


afn = AFN()

exemplos = ["01", "001", "010", "0001", "111", "10", "100"]
results = {s: afn.accepts(s) for s in exemplos}

for s, result in results.items():
    print(f"A string '{s}' é aceita? {result}")
