''' 
QUESTÃO 7

Implemente um AFN que reconheça strings que comecem com '01' e terminem com '10'.

'''

class AFN:
    def __init__(self):
        self.transitions = {
            (0, '0'): {1},
            (1, '1'): {2},
            (2, '0'): {2},
            (2, '1'): {3},
            (3, '0'): {4}
        }
        self.initial_state = 0
        self.accept_states = {4}

    def _move(self, states, symbol):
        next_states = set()
        for state in states:
            if (state, symbol) in self.transitions:
                next_states.update(self.transitions[(state, symbol)])
        return next_states

    def accepts(self, string):
        current_states = {self.initial_state}
        
        for symbol in string:
            current_states = self._move(current_states, symbol)
            if not current_states:
                return False
        
        return bool(current_states & self.accept_states)

afn = AFN()
exemplo = ["0110", "0101010", "0010", "1010", "0110"]

for s in exemplo:
    print(f"String '{s}' é aceita? {afn.accepts(s)}")


