''' 
QUESTÃO 15

Crie um AFN que aceite strings binárias onde as substrings "11" e "00" não aparecem.

'''

from automata.fa.nfa import NFA

nfa = NFA(
    states={'q0', 'q1'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q1'},
        'q1': {'a': 'q0', 'b': 'q0'},
    },
    initial_state='q0',
    final_states={'q0'}
)

def is_accepted(string):
    return nfa.accepts_input(string)

test_strings = ['a', 'b', 'ab', 'ba', 'aa', 'bb', 'aaa', 'aab', 'abba', '']
for s in test_strings:
    result = is_accepted(s)
    print(f"A string '{s}' é aceita? {result}")
