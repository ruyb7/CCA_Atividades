''' 
QUESTÃO 23

Construa um AFN que aceite qualquer string que contenha a sequência "101" ou "110" sobre {0, 1}.

'''

class NFA:
    def __init__(self):
        self.start_state = 0
        self.accept_states = {3, 4}
        self.transition_table = {
            0: {'1': {1}},
            1: {'0': {2}, '1': {3}},
            2: {'1': {4}},
            3: {},
            4: {}
        }

    def move(self, state, symbol):
        return self.transition_table.get(state, {}).get(symbol, set())

    def accepts(self, input_string):
        current_states = {self.start_state}
        for symbol in input_string:
            next_states = set()
            for state in current_states:
                next_states.update(self.move(state, symbol))
            current_states = next_states
        return not current_states.isdisjoint(self.accept_states)

nfa = NFA()

test_strings = [
    "00100",
    "101010",
    "11000",
    "1001",
    "1110",
    "0000",
    "111111",
    "010101"
]

for s in test_strings:
    result = nfa.accepts(s)
    print(f"A string '{s}' é aceita? {result}")
