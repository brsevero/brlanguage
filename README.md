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
   
   FUNCAO PRINCIPAL(){
   
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

1. Especificação de Tipos:
   - A linguagem é tipada estaticamente, o que significa que toda variavél precisa indicar o seu tipo ao ser declarada e esse tipo fica inculado a varíavel durante toda a sua vida;
   - Lista de tipos definidos em BRLanguage:
      1. INTEIRO - Inteiro de x tamanho em bits
      1. FLUTUANTE - Ponto flutuante de x tamanho em bits
      1. CARACTERE - Caractere
      1. BOOLEANO - Booleano
      1. FRASE - cadeia de caractere de x tamanho máximo de caracteres
      1. *tipo_do vetor* *identificador_do_vetor*[tamanho] - Arranjos unidimencionais de qualquer tipo

1. Operação Suportadas:
   - Todos os tipos primitivos suportam as operações descritas na tabela abaixo, com os valores de seu tipo específico, ou segundo as regras de coerções:
     |**Tipo**|**Operações Suportadas**|
     | :---: | :---: |
     | INTEIRO | atribuição, aritméticas, relacionais |
     | FLUTUANTE | atribuição, aritméticas, relacionais |
     | CARACTERE | atribuição, relacionais |
     | BOOLEANO | atribuição, relacionais |
     | FRASE | atribuição, relacionais, concatenação |
     | *vetor* | atribuição |


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

