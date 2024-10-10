''' 
QUESTÃO 18

Desenvolva um AFD que reconheça a linguagem de strings sobre {0, 1} com número ímpar de '0's e
'1's.


'''

from automata.fa.dfa import DFA

afd = DFA(
    states={'q00', 'q01', 'q10', 'q11'}
    input_symbols={'0', '1'},
    transitions={
        'q00': {'0': 'q10', '1': 'q01'},
        'q01': {'0': 'q11', '1': 'q00'},
        'q10': {'0': 'q00', '1': 'q11'},
        'q11': {'0': 'q01', '1': 'q10'},
    },
    initial_state='q00',
    final_states={'q11'}
)

def is_accepted(binary_string):
    return afd.accepts_input(binary_string)

test_strings = ['0', '1', '00', '11', '01', '10', '001', '110', '101', '0001', '1111', '0101', '1010']
for s in test_strings:
    result = is_accepted(s)
    print(f"A string '{s}' é aceita? {result}")
