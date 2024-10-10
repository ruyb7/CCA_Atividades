''' 
QUESTÃO 20

Implemente um AFD para strings sobre {a, b} onde a sequência 'ab' aparece exatamente uma vez.

'''

class AFD:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.initial_state = 'q0'
        self.final_state = 'q2'
        self.transitions = {
            'q0': {'a': 'q1', 'b': 'q0'},
            'q1': {'a': 'q1', 'b': 'q2'},
            'q2': {'a': 'q3', 'b': 'q2'},
            'q3': {'a': 'q3', 'b': 'q3'},
        }

    def process_input(self, input_string):
        current_state = self.initial_state

        for symbol in input_string:
            if symbol in self.transitions[current_state]:
                current_state = self.transitions[current_state][symbol]
            else:
                return False

        return current_state == self.final_state

afd = AFD()

test_strings = ['ab', 'abab', 'aab', 'b', 'aaab', 'aabb', 'ababc', 'abbb', 'baba', 'aaaab']
results = {s: afd.process_input(s) for s in test_strings}

for s, result in results.items():
    print(f"A string '{s}' é aceita: {result}")
