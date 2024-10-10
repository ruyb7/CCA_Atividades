''' 
QUESTÃO 21

- Implemente um AFN que aceite todas as strings sobre {a, b} que tenham um 'a' após cada 'b'

'''

class AFN:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.initial_state = 'q0'
        self.final_states = {'q0', 'q2'}
        self.transitions = {
            'q0': {'a': {'q0'}, 'b': {'q1'}},
            'q1': {'a': {'q0'}, 'b': {'q3'}},
            'q2': {'a': {'q0'}, 'b': {'q1'}},
            'q3': {'a': set(), 'b': set()},
        }

    def process_input(self, input_string):
        current_states = {self.initial_state}

        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if symbol in self.transitions[state]:
                    next_states.update(self.transitions[state][symbol])
            current_states = next_states

            if 'q3' in current_states:
                return False

        return any(state in self.final_states for state in current_states)

afn = AFN()

test_strings = ['a', 'b', 'aa', 'ab', 'ba', 'bb', 'abab', 'aaab', 'aabab', 'baba', 'aaa', 'bab', 'abbb', 'bbab', 'aab']
results = {s: afn.process_input(s) for s in test_strings}

for s, result in results.items():
    print(f"A string '{s}' é aceita: {result}")
