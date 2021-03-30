from sly import Lexer

class analisador_lexico(Lexer):

    tokens = {FUNCAO, ATRIBUICAO, IGUALADOR, NUMERO, MAIS, MENOS, VEZES, DIVIDIR, PARENTESES_ESQ, PARENTESES_DIR,CHAVE_ESQ, CHAVE_DIR4, SE, MAS_SE, SENAO, ENQUANTO, IDENTADOR, IMPRIMIR}

    literals = { '=', '+', '-', '/', '*', '(', ')','{','}', ',', ';'}

    ignore = ' \t'
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'

    VARIAVEL = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ATRIBUICAO = r'='
    IGUALADOR = r'=='
    INTEIRO = r'\d+'
    MAIS = r'\+'
    MENOS = r'-'
    VEZES = r'\*'
    DIVIDIR = r'/'
    PARENTESES_ESQ = r'\('
    PARENTESES_DIR = r'\)'

    VARIAVEL['SE'] = SE
    VARIAVEL['MAS_SE'] = MAS_SE
    VARIAVEL['SENAO'] = SENAO
    VARIAVEL['ENQUANTO'] = ENQUANTO
    VARIAVEL['IDENTADOR'] = IDENTADOR
    VARIAVEL['IMPRIMIR'] = IMPRIMIR


    def NUMERO(self, t):
        t.value = int(t.value)
        return t

    def ignore_newline(self, t):
        self.lineno += len(t.value)    


if __name__ == '__main__':
    data = """VAZIO PRINCIPAL(){
   IMPRIMIR("Alô Mundo!");
   RETORNE ;
}"""
    lexer = analisador_lexico()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))