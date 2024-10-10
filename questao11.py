''' 
QUESTÃO 11

Construa um AFD para uma linguagem sobre o alfabeto {a, b}, que reconheça strings com um
número ímpar de 'a's.


'''

class AFD:
    def __init__(self):
        self.states = {'q0', 'q1'}
        self.start_state = 'q0'
        self.accept_states = {'q1'}

    def transition(self, state, symbol):
        if state == 'q0':
            if symbol == 'a':
                return 'q1'
            elif symbol == 'b':
                return 'q0'
        elif state == 'q1':
            if symbol == 'a':
                return 'q0'
            elif symbol == 'b':
                return 'q1'
        return None

    def accepts(self, string):
        current_state = self.start_state
        for symbol in string:
            current_state = self.transition(current_state, symbol)
            if current_state is None:
                return False 

        return current_state in self.accept_states


afd = AFD()

exemplos = ["a", "b", "ab", "aab", "abb", "aa", "aaa", "aabbaa", "bbab"]
results = {s: afd.accepts(s) for s in exemplos}

for s, result in results.items():
    print(f"A string '{s}' é aceita? {result}")
