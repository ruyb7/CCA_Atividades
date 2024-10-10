''' 
QUESTÃO 17

Implemente em Python a conversão de um AFN para um AFD para um autômato que reconhece
strings terminadas em '01'.


'''

from automata.fa.nfa import NFA
from automata.fa.dfa import DFA

nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q1', '1': 'q2'},
        'q2': {'0': 'q1', '1': 'q0'},
    },
    initial_state='q0',
    final_states={'q2'}
)

afd = DFA.from_nfa(nfa)

def is_accepted(string):
    return afd.accepts_input(string)

test_strings = ['0', '1', '01', '10', '001', '110', '101', '0001', '0101', '1101', '1110']
for s in test_strings:
    result = is_accepted(s)
    print(f"A string '{s}' é aceita? {result}")
