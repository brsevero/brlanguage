from sly import Lexer

class analisador_lexico(Lexer):

    tokens = {VARIAVEL, FUNCAO, RESERVADA, ATRIBUICAO, IGUALADOR, VAZIO, INTEIRO, FLUTUANTE, CARACTERE, BOOLEANO, CARACTERES, MAIS, MENOS, VEZES,DIVIDIR, PARENTESES_ESQ, PARENTESES_DIR}
    # SE, MAS_SE, SENAO, ENQUANTO, IDENTADOR, IMPRIMIR
    literals = { '=', '+', '-', '*', '/', '(', ')','{','}','>','<','==','!=','>=','<=', ',', ';',"'","\"",}

    ignore = ' \t'
    ignore_comment = r'\#.*'

    @_(r'\n+')
    def ignore_newline(self, t):   
        self.lineno += len(t.value)

    @_(r'FUNCAO [a-zA-Z_][a-zA-Z0-9_]*')
    def FUNCAO(self, t):
        t.value = t.value[7:]
        return t

    VARIAVEL = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ATRIBUICAO = r'='
    IGUALADOR = r'=='
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
    VARIAVEL['SE'] = RESERVADA
    VARIAVEL['MAS_SE'] = RESERVADA
    VARIAVEL['SENAO'] = RESERVADA
    VARIAVEL['ENQUANTO'] = RESERVADA
    VARIAVEL['IDENTADOR'] = RESERVADA
    VARIAVEL['IMPRIMIR'] = RESERVADA
    VARIAVEL['PRINCIPAL'] = RESERVADA
    VARIAVEL['FUNCAO'] = RESERVADA
    VARIAVEL['VAZIO'] = RESERVADA
    VARIAVEL['RETORNE'] = RESERVADA

    @_(r'\d+')
    def INTEIRO(self, t):
        t.value = int(t.value)
        return t

    def ignore_newline(self, t):
        self.lineno += len(t.value)    


if __name__ == '__main__':
    data = """VAZIO FUNCAO fibonacci(INTEIRO limite){
   INTEIRO contador;
   INTEIRO um;
   INTEIRO dois;
   INTEIRO tres;

   um = 1;
   dois = 1;

   if(limite == 0){
      IMPRIMIR("0");
   }
   ENQUANTO(contador < limite){
      SE(contador < 2){
         IMPRIMIR("1");
      }
      SENAO{
         tres = um + dois;
         um = dois;
         dois = tres;
         IMPRIMIR(tres +++ " ");
      }
   }
   contador = contador + 1;
}
"""
    lexer = analisador_lexico()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))