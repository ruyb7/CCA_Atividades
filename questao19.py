''' 
QUESTÃO 19

Construa um AFN que reconheça a linguagem de todas as strings binárias que contenham a
substring '010'.



'''

class AFN:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.initial_state = 'q0'
        self.final_state = 'q3'
        self.transitions = {
            'q0': {'0': {'q1'}, '1': {'q0'}},
            'q1': {'0': {'q1'}, '1': {'q2'}},
            'q2': {'0': {'q3'}, '1': {'q0'}},
            'q3': {'0': {'q3'}, '1': {'q3'}},
        }

    def epsilon_closure(self, states):
        closure = set(states)
        return closure

    def process_input(self, input_string):
        current_states = {self.initial_state}

        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if symbol in self.transitions[state]:
                    next_states.update(self.transitions[state][symbol])
            current_states = next_states

        return self.final_state in current_states

afn = AFN()

test_strings = ['110', '1010', '001010', '111', '0101', '000', '100100']
results = {s: afn.process_input(s) for s in test_strings}

for s, result in results.items():
    print(f"A string '{s}' é aceita: {result}")
