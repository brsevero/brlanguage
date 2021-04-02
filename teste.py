import re

class Lexer():
    def __init__(self):
        #self.file = file
        self.linhas = int(0)
        self.colunas = int(0)

    def regras(self, token):
        NAO_RECONHECIDO = (0, 'nao reconhecido')
        VARIAVEL = (1, 'variavel')
        IGUALADOR = (2, 'igualador')
        MAIOR_QUE = (3, 'maior que')
        MENOR_QUE = (4, 'menor que')
        DIFERENTE = (5, 'diferente')
        MAIOR_IGUAL = (6, 'maior igual')
        MENOR_IGUAL = (7, 'menor igual')
        ATRIBUICAO = (8, 'atribuicao')
        NUMERO = (9, 'tipo: numero')
        CARACTERE = (10, 'tipo: caractere')
        CARACTERES = (11, 'tipo: caracteres')
        MAIS = (12,'mais')
        MENOS = (13, 'menos')
        VEZES = (14, 'vezes')
        DIVIDIR = (15, 'dividir')
        PARENTESES_ESQ = (16, 'parenteses esquerdo')
        PARENTESES_DIR = (17, 'parenteses direito')
        CHAVE_ESQ = (18, 'chave esquerda')
        CHAVE_DIR = (19, 'chave direita')
        CONCHETE_DIR = (20, 'conchete direito')
        CONCHETE_ESQ = (21, 'conchete esquerdo')
        VIRGULA = (22, 'virgula')
        PONTO_VIR = (23, 'ponto e virgula')
        ASPAS = (24, 'aspas')
        ASPAS_DU = (25, 'aspas duplas')
        CONCATENACAO = (26, 'concatenacao')
        FUNCAO = (27, 'funcao')
        PRINCIPAL = (28, 'principal')
        LER = (29, 'leitura')
        IMPRIMIR = (30, 'escrita')
        RETORNE = (31, 'retorno')
        SE = (32, 'condicional se')
        MAS_SE = (33, 'condicional mas se')
        SENAO = (34, 'condicional senao')
        FAZER = (35, 'repeticao faz')
        ENQUANTO = (36, 'repeticao enquanto')
        ITERADOR = (37, 'repeticao iterador')
        BOOLEANO = (38, 'tipo: booleano')
        NAO = (39, 'logico nao')
        E = (40, 'logico e')
        OU = (41, 'logico ou')
        VAZIO = (42, 'tipo: vazio')
        INTEIRO = (43, 'tipo: inteiro')
        BRANCO = (44, 'branco')


        palavras_reservadas = {
            'FUNCAO' : FUNCAO,
            'PRINCIPAL' : PRINCIPAL,
            'LER' : LER,
            'IMPRIMIR' : IMPRIMIR,
            'RETORNE' : RETORNE,
            'SE' : SE,
            'MAS_SE' : MAS_SE,
            'SENAO' : SENAO,
            'FAZER' : FAZER,
            'ENQUANTO' : ENQUANTO,
            'ITERADOR' : ITERADOR,
            'VERDADEIRO' : BOOLEANO,
            'FALSO' : BOOLEANO,
            'NAO' : NAO,
            'E' : E,
            'OU' : OU,
            'VAZIO' : VAZIO,
            'INTEIRO' : INTEIRO,
        }

        regras = {
            '[a-zA-Z][a-zA-Z0-9_]*' : VARIAVEL,
            '\==' : IGUALADOR,
            '\>' : MAIOR_QUE,
            '\<' : MENOR_QUE,
            '\!=' : DIFERENTE,
            '\>=' : MAIOR_IGUAL,
            '\<=' : MENOR_IGUAL,
            '\=' : ATRIBUICAO,
            '\d+' : NUMERO,
            '[\'|\"]\S[\'|\"]' : CARACTERE,
            '[\'\"].*?[\'\"]' : CARACTERES,
            '\+' : MAIS,
            '\-' : MENOS,
            '\*' : VEZES,
            '\/' : DIVIDIR,
            '\(' : PARENTESES_ESQ,
            '\)' : PARENTESES_DIR,
            '\{' : CHAVE_ESQ,
            '\}' : CHAVE_DIR,
            '\[' : CONCHETE_DIR,
            '\]' : CONCHETE_ESQ,
            '\,' : VIRGULA,
            '\;' : PONTO_VIR,
            '\'' : ASPAS,
            '\"' : ASPAS_DU,
            '\&' : CONCATENACAO,
            ' \t' : BRANCO
            }

        for i in regras:
            if re.match(' \t', token):
                return regras[i]
        
        for i in palavras_reservadas:
            if i == token:
                return palavras_reservadas[i]
    def criar_tokens(self, line):
        tokens = []
        lexema = ""
        for i in line:
            #print(i)
            lexema += i
            if i == ' ':
                print('entrou')
                tokens.append(lexema)
                lexema = ""
        return tokens




if __name__ == '__main__':
    a = Lexer()
    with open('principal.brl', 'r') as file:
        for linhas in file:
            print(linhas)
            print(a.criar_tokens(linhas))
            input()