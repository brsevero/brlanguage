from sly import Lexer

class Meulexico(Lexer):

    tokens = {VARIAVEL, ATRIBUICAO, NUMERO, MAIS, MENOS, VEZES,DIVIDIR, PARENTESES_ESQ, PARENTESES_DIR, SE, MAS_SE, SENAO, ENQUANTO, IDENTADOR}

    ignore = ' \t'
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'

    VARIAVEL = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ATRIBUICAO = r'='
    NUMERO = r'\d+'
    MAIS = r'\+'
    MENOS = r'-'
    VEZES = r'\*'
    DIVIDIR = r'/'
    PARENTESES_ESQ = r'\('
    PARENTESES_DIR = r'\)'

    VARIAVEL['if'] = SE
    VARAIVEL['elif'] = MAS_SE
    VARIAVEL['else'] = SENAO
    VARIAVEL['while'] = ENQUANTO
    VARIAVEL['for'] = IDENTADOR

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

