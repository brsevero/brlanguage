from sly import Lexer

class analisador_lexico(Lexer):

    tokens = {VARIAVEL, ATRIBUICAO, CARACTERE, CARACTERES,  MAIS, MENOS, VEZES, DIVIDIR, PARENTESES_ESQ, PARENTESES_DIR, CHAVE_ESQ, CHAVE_DIR,
    MAIOR_QUE, MENOR_QUE, IGUALADOR, DIFERENTE, MAIOR_IGUAL, MENOR_IGUAL, SE, MAS_SE, SENAO, ENQUANTO, IDENTADOR, IMPRIMIR,  INTEIRO, VIRGULA, PONTO_VIR, ASPAS, ASPAS_DU, FUNCAO, RESERVADA, CONCATENACAO, BOOLEANO, VAZIO, NUMERO}

    literals = { '=', '+', '-', '*', '/', '(', ')','{','}','>','<','==','!=','>=','<=', ',', ';',"'","\"",}

    ignore = ' \t'
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'


    VARIAVEL = r'[a-zA-Z][a-zA-Z0-9_]*'
    ATRIBUICAO = r'\='
    NUMERO = r'\d+'
    CARACTERE = r'[\'|\"]\S[\'|\"]'
    CARACTERES = r'[\'\"].*?[\'\"]'
    MAIS = r'\+'
    MENOS = r'\-'
    VEZES = r'\*'
    DIVIDIR = r'\/'
    PARENTESES_ESQ = r'\('
    PARENTESES_DIR = r'\)'
    CHAVE_ESQ = r'\{'
    CHAVE_DIR = r'\}'
    MAIOR_QUE = r'\>'
    MENOR_QUE = r'\<'
    IGUALADOR = r'\=='
    DIFERENTE = r'\!='
    MAIOR_IGUAL = r'\>='
    MENOR_IGUAL = r'\<='
    VIRGULA = r'\,'
    PONTO_VIR = r'\;'
    ASPAS = r'\''
    ASPAS_DU = r'\"'
    CONCATENACAO = r'\++'


    VARIAVEL['FUNCAO'] = RESERVADA
    VARIAVEL['PRINCIPAL'] = RESERVADA
    VARIAVEL['LER'] = RESERVADA
    VARIAVEL['IMPRIMIR'] = RESERVADA
    VARIAVEL['RETORNE'] = RESERVADA
    VARIAVEL['SE'] = RESERVADA
    VARIAVEL['MAS_SE'] = RESERVADA
    VARIAVEL['SENAO'] = RESERVADA
    VARIAVEL['FAZ'] = RESERVADA
    VARIAVEL['ENQUANTO'] = RESERVADA
    VARIAVEL['ITERADOR'] = RESERVADA
    VARIAVEL['VERDADE'] = RESERVADA
    VARIAVEL['FALSO'] = RESERVADA
    VARIAVEL['NAO'] = RESERVADA
    VARIAVEL['E'] = RESERVADA
    VARIAVEL['OU'] = RESERVADA
    VARIAVEL['ENQUANTO'] = RESERVADA
    VARIAVEL['FAZER ENQUANTO'] = RESERVADA
    VARIAVEL['FALSO'] = BOOLEANO
    VARIAVEL['VERDADEIRO'] = BOOLEANO
    VARIAVEL['VAZIO'] = VAZIO
    VARIAVEL['INTEIRO'] = INTEIRO
    
    


    def NUMERO(self, t):
        t.value = int(t.value)
        return t

    def ignore_newline(self, t):
        self.lineno += len(t.value)    


if __name__ == '__main__':
    data = """VAZIO fibonacci(INTEIRO limite){
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
         IMPRIMIR(tres ++ " ");
      }
   }
   contador = contador + 1;
}

VAZIO PRINCIPAL(){
   INTEIRO limite;
   LER(INTEIRO, limite);
   fibonacci(limite);
   RETORNE ;
}
}"""
    lexer = analisador_lexico()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))