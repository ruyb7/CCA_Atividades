''' 
QUESTÃO 1

Crie um autômato finito determinístico (AFD) que reconheça a linguagem sobre o alfabeto {0, 1}, 
onde todas as strings terminam com "1". 

'''

class AFD:
    def __init__(self):
        self.state = 0

    def transition(self, symbol):
        if self.state == 0:
            if symbol == '1':
                self.state = 1
            elif symbol == '0':
                self.state = 0
        elif self.state == 1:
            if symbol == '1':
                self.state = 1
            elif symbol == '0':
                self.state = 0

    def accepts(self, string):
        for symbol in string:
            self.transition(symbol)
        return self.state == 1


afd = AFD()
print(afd.accepts("110"))
print(afd.accepts("100"))
print(afd.accepts("101"))
print(afd.accepts("1"))
print(afd.accepts("0"))
print(afd.accepts("11"))
