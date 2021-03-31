from sly import Lexer

class analisador_lexico(Lexer):

    tokens = {VARIAVEL, FUNCAO, ATRIBUICAO, IGUALADOR, INTEIRO, FLUTUANTE, CARACTERE, BOOLEANO, CARACTERES, MAIS, MENOS, VEZES,DIVIDIR, PARENTESES_ESQ, PARENTESES_DIR}
    # SE, MAS_SE, SENAO, ENQUANTO, IDENTADOR, IMPRIMIR
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';'}

    ignore = ' \t'
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'

    VARIAVEL = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ATRIBUICAO = r'='
    IGUALADOR = r'=='
    INTEIRO = r'\d+'
    # FLUTUANTE = r'\d+'
    CARACTERE = r'[\'|\"]\S[\'|\"]'
    CARACTERES = r'[\'\"].*?[\'\"]'
    MAIS = r'\+'
    MENOS = r'-'
    VEZES = r'\*'
    DIVIDIR = r'/'
    PARENTESES_ESQ = r'\('
    PARENTESES_DIR = r'\)'



    VARIAVEL['FALSO'] = BOOLEANO
    VARIAVEL['VERDADEIRO'] = BOOLEANO
    VARIAVEL['SE'] = FUNCAO
    VARIAVEL['MAS_SE'] = FUNCAO
    VARIAVEL['SENAO'] = FUNCAO
    VARIAVEL['ENQUANTO'] = FUNCAO
    VARIAVEL['IDENTADOR'] = FUNCAO
    VARIAVEL['IMPRIMIR'] = FUNCAO
    VARIAVEL['PRINCIPAL'] = FUNCAO

    def NUMERO(self, t):
        t.value = int(t.value)
        return t

    def ignore_newline(self, t):
        self.lineno += len(t.value)    


if __name__ == '__main__':
    data = """('alo mundo')
"""
    lexer = analisador_lexico()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))