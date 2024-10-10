''' 
QUESTÃO 16  

 Construa um AFD para reconhecer strings sobre {0, 1} onde os '0's aparecem em blocos
consecutivos.

'''

from automata.fa.dfa import DFA

afd = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q1', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q2'},
    },
    initial_state='q0',
    final_states={'q0', 'q1'}
)

def is_accepted(binary_string):
    return afd.accepts_input(binary_string)

test_strings = ['0', '1', '00', '11', '01', '10', '1100', '0001', '001', '111', '1010']
for s in test_strings:
    result = is_accepted(s)
    print(f"A string '{s}' é aceita? {result}")
