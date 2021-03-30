from sly import Lexer

class Meulexico(Lexer):
    #lista de tokens que eu preciso obrigatoriamente e sempre em UPCASE
    #lista de coisas ignoradas em ER sempre com aspas simples
    #lista de ER para os tokens

    tokens = {ID, ATRIBUICAO, NUMERO, SOMA, IF, ELSE, WHILE}

    #ignorar coisa só precisa comecar com "ignore_"
    ignore = ' \t'
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ATRIBUICAO = r'='
    NUMERO = r'\d+'
    SOMA = r'\+'

    # Special cases
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE

    def NUMERO(self, t):
        t.value = int(t.value)
        return t

    def ignore_newline(self, t):
        self.lineno += len(t.value)    


if __name__ == '__main__':
    texto = """x = 1 + 2
            #comentario"""
    compilador = Meulexico()
    #lista_de_tokens = []
    for x in compilador.tokenize(texto):
        #lista_de_tokens.append((x.type,x.value))
        print('tipo = %r, valor = %r' % (x.type,x.value))
    #print(lista_de_tokens)
    print(compilador.lineno)
    print(compilador)

