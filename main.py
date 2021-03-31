from lexico import analisador_lexico

if __name__ == '__main__':
    with open('shell.brl','r') as data:
        lexer = analisador_lexico()
        for linhas in data:
            for tok in lexer.tokenize(linhas):
                print('type=%r, value=%r, linha = %i' % (tok.type, tok.value, lexer.linha))