from sly import Lexer

class analisador_lexico(Lexer):

    tokens = {VARIAVEL, ATRIBUICAO, CARACTERE, CARACTERES,  MAIS, MENOS, VEZES, DIVIDIR, PARENTESES_ESQ, PARENTESES_DIR, CHAVE_ESQ, CHAVE_DIR,
    MAIOR_QUE, MENOR_QUE, CONCHETE_DIR,CONCHETE_ESQ, IGUALADOR, DIFERENTE, MAIOR_IGUAL, MENOR_IGUAL, SE, MAS_SE, SENAO, ENQUANTO, IDENTADOR, IMPRIMIR,  INTEIRO, VIRGULA, PONTO_VIR, ASPAS, ASPAS_DU, FUNCAO, RESERVADA, CONCATENACAO, BOOLEANO, VAZIO, NUMERO}

    literals = { '=', '+', '-', '*', '/', '(', ')','{','}','[',']','>','<','==','!=','>=','<=', ',', ';',"'","\"",}

    ignore = ' \t'
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'


    VARIAVEL = r'[a-zA-Z][a-zA-Z0-9_]*'
    IGUALADOR = r'\=='
    MAIOR_QUE = r'\>'
    MENOR_QUE = r'\<'
    DIFERENTE = r'\!='
    MAIOR_IGUAL = r'\>\='
    MENOR_IGUAL = r'\<='
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
    CONCHETE_DIR = r'\['
    CONCHETE_ESQ = r'\]'
    VIRGULA = r'\,'
    PONTO_VIR = r'\;'
    ASPAS = r'\''
    ASPAS_DU = r'\"'
    CONCATENACAO = r'\&'


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
    VARIAVEL['INTEIRO'] = RESERVADA
    
    


    def NUMERO(self, t):
        t.value = int(t.value)
        return t

    def ignore_newline(self, t):
        self.lineno += len(t.value)    


if __name__ == '__main__':
    data = """INTEIRO FUNCAO shell(INTEIRO array[], INTEIRO tamanho){
   INTEIRO i;
   INTEIRO j;
   INTEIRO valor;
   INTEIRO h;

   ITERADOR(h = 1, h < tamanho, h = h * 3 + 1){
      #so alterando o h
   }

   ITERADOR( h = h/3 , h < 1 , ){
      ITERADOR(i = h, i < tamanho, i = i + 1){
         valor = array[i];
         ITERADOR( j = i ­- h , j >= 0 E valor < array[j] , j = j ­- h){
            array[j + h] = array[j];
         }

         array[j+h] = valor;
      }
   }

   RETORNE array;
}

VAZIO FUNCAO PRINCIPAL(){
   INTEIRO vetor[10];
   INTEIRO saida[10];

   vetor = [9, 8, 3, 2, 5, 1, 4, 7, 6, 0];

   saida = shell(vetor, 10);
}
   """
    lexer = analisador_lexico()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))