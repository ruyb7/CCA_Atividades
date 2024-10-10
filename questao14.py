''' 
QUESTÃO 14

Crie um AFN que aceite strings binárias onde as substrings "11" e "00" não aparecem.


'''

from automata.fa.nfa import NFA

nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q2'},
        'q1': {'0': 'q1', '1': 'q0'},
        'q2': {'0': 'q0', '1': 'q2'},
    },
    initial_state='q0',
    final_states={'q0', 'q1', 'q2'}
)

def is_accepted(binary_string):
    return nfa.accepts_input(binary_string)

test_strings = ['0', '1', '01', '10', '001', '110', '0101', '1010', '000', '111']
for s in test_strings:
    result = is_accepted(s)
    print(f"A string '{s}' é aceita? {result}")
