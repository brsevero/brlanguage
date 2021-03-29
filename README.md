# BRLanguage
### Programming Language Project for Compiladores 2020.1 - UFAL
#### A BRLanguage foi pensanda para ser uma linguagem simples, fácil de implementar algorítmos mais básico e para aprender conceitualmente sobre programação, além de ser toda em português o que permite um aprendizado de conceitos como tipos de dados e estruturas de controles de forma mais simples.

1. Características Gerais:
   - A linguagem é toda em português;
   - A linguagem pertece ao paradigma Imperativo;
   - O método utilizado de implementação é a compilação.
   
1. Estrutura Geral de Um Programa
   - Para se criar um programa em BRLanguage deve-se escrever um código, obdecendo as regras da linguagem, e colocar a extensão ".brl";
   - BRLanguage funciona com um conjunto de funções, onde a função que começa o programa é denominada "Principal". A função Principal retorna um tipo definido pelo programador e possui a sintaxe abaixo:
   
   ```
   
   funcao principal(){
   
   };
   
   ```
   - Ao final de cada comando deve-se colocar o delimitador de instrução ";" ;
   - Os delimitadores de escopo são:
     1. Inicar: "{";
     1. Finalizar: "}";
   - Um programa em .brl deve seguir as regras de identação para um melhor entendimento;
   - A linguagem permite comentários por linha utilizando o delimitador de comentários: "#".

1. Características Léxicas:
   - Identificadores não podem conter numeros;
   - Identificadores são em lowercase, ou seja, em minúsculo;
   - Identificadores devem ter no máximo tamanho 8 e não podem conter caracteres especiais, apenas o alfabeto latino padrão, e não devem coincidir com as palavras reservadas da linguagem.
   - Lista de palavras reservadas da linguagem:
     | **Especificação de Tipo** | **Função** | **Comandos** | **Operadores Lógicos** |
     | :------:| :------: | :------: | :------: |
     | INTEIRO | FUNCAO | SE | VERDADE |
     | FLUTUANTE | PRINCIPAL | SENAO | FALSO |
     | CARACTERE |  | ENTAO | NAO |
     | BOOLEANO |  | FAÇA | E |
     | FRASE |  | ENQUANTO | OU |
     | VETOR |  | teste3 |  |


1. Tipos de dados primitivos:
   1. inteiro - INTEIRO
   1. ponto flutuante - FLUTUANTE
   1. caractere - CARACTERE
   1. booleano - BOOLEANO
   1. cadeia de caractere - FRASE
   1. Arranjos unidimencionais - VETOR

1. Conjunto de operadores: #colocar a ordem de precedência e associatividade
   1. Aritméticos:
      1. "*" multiplicação
      1. "/" divisão
      1. "-" subtração
      1. "+" adição
      1. "%" resto da divisão
    1. Relacionais:
       1. inteiros:
          1. "=="
          1. "!="
          1. "<"
          1. ">"
          1. "<="
          1. ">="
        1. Caractere:
           1. Não Possui
     1. Cadeia de caracteres:
        1. Não possui
     1. Lógicos:
        1. "!" negação
        1. "&&" and
        1. "||" or
     1. Concatenação:
        1. Caractere e Cadeia de caracteres:
           1. "+"
        1. Numéricos e Booleanos:
           1. Não possui

1. Operacoes de cada tipo:
   1. inteiro - INT:
 
3. Contantes Literais de cada Tipo:

funcao bruno(argumentos):
  imprime("Olá mundo!\n");

