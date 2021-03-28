import BasicLexer as bl
lexer = bl.BasicLexer()

text = "1 + 2"
print(lexer.tokenize(text))
lexer.tokenize(text)