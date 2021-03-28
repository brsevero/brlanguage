from sly import Lexer

class Meulexico(Lexer):
    #lista de tokens que eu preciso obrigatoriamente
    #lista de coisas ignoradas em ER sempre com aspas simples
    #lista de ER para os tokens

    tokens = {ID, ATRIBUICAO, NUMERO, SOMA}

    ignore = ' \t'

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ATRIBUICAO = r'='
    NUMERO = r'\d+'
    SOMA = r'\+'


if __name__ == '__main__':
    texto = "x = 1 + 2"
    compilador = Meulexico()
    #lista_de_tokens = []
    for x in compilador.tokenize(texto):
        #lista_de_tokens.append((x.type,x.value))
        print('tipo = %r, valor = %r' % (x.type,x.value))
    #print(lista_de_tokens)

