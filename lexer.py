from sly import Lexer

class analisador_lexico(Lexer):

    tokens = {VARIAVEL, FUNCAO, ATRIBUICAO, IGUALADOR, NUMERO, MAIS, MENOS, VEZES,DIVIDIR, PARENTESES_ESQ, PARENTESES_DIR, SE, MAS_SE, SENAO, ENQUANTO, IDENTADOR, IMPRIMIR}

    literals = { '=', '+', '-', '/', 
                '*', '(', ')', ',', ';'}

    ignore = ' \t'
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'

    VARIAVEL = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ATRIBUICAO = r'='
    IGUALADOR = r'=='
    NUMERO = r'\d+'
    MAIS = r'\+'
    MENOS = r'-'
    VEZES = r'\*'
    DIVIDIR = r'/'
    PARENTESES_ESQ = r'\('
    PARENTESES_DIR = r'\)'

    FUNCAO['if'] = SE
    FUNCAO['elif'] = MAS_SE
    FUNCAO['else'] = SENAO
    FUNCAO['while'] = ENQUANTO
    FUNCAO['for'] = IDENTADOR
    FUNCAO['print'] = IMPRIMIR


    def NUMERO(self, t):
        t.value = int(t.value)
        return t

    def ignore_newline(self, t):
        self.lineno += len(t.value)    


if __name__ == '__main__':
    data = """IMPRIMIR"""
    lexer = analisador_lexico()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))