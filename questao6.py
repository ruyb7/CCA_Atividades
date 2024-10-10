''' 
QUESTÃO 6

Construa um autômato finito não-determinístico (AFN) que aceite strings que contenham pelo
menos um '0' sobre o alfabeto {0, 1}.

'''

class AFN:
    def __init__(self):
        self.estados = {'q0', 'q1', 'qrej'}
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q1'}
        self.transicoes = {
            ('q0', '0'): {'q0', 'q1'},
            ('q0', '1'): {'q0'},
            ('q1', '0'): {'q1'},
            ('q1', '1'): {'q1'}
        }
        self.estados_atuais = {self.estado_inicial}

    def processa_string(self, string):
        for simbolo in string:
            novos_estados = set()
            for estado in self.estados_atuais:
                if (estado, simbolo) in self.transicoes:
                    novos_estados.update(self.transicoes[(estado, simbolo)])
            self.estados_atuais = novos_estados
            if not self.estados_atuais:
                return False
        return any(estado in self.estados_aceitacao for estado in self.estados_atuais)

def testar_afn(strings):
    afn = AFN()
    for string in strings:
        resultado = afn.processa_string(string)
        print(f"String '{string}': {'Aceita' if resultado else 'Rejeitada'}")

exemplo = ['001', '110', '111', '0000', '']
testar_afn(exemplo)
