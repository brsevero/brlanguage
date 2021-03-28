from sly import Lexer

class BasicLexer(Lexer):

    tokens = { NAME, NUMBER, STRING }
    ignore = '\t ' #escape de espaçamento
    literals = { '=', '+', '-', '/', 
                '*', '(', ')', ',', ';'}
  
  
    # Define os tokens como expressões regulares
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Define que a string vem entre aspas simples os duplas
    STRING = r'\".*?\"'

  
    # token de NUMBER
    # + indica uma ou mais ocorrências de elemento precedente
    @_(r'\d+')
    def NUMBER(self, t):
        
        # converte em inteiro
        t.value = int(t.value)
        print(t.value)
        return t
  
    # token de COMMENT
    # * indica zero ou mais ocorrências de elemento precedente
    @_(r'//.*')
    def COMMENT(self, t):
        pass
  
    # token nova linha (quebra de linha)
    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')
        