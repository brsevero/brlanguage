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
     - INTEIRO - Inteiro de x tamanho em bits
     - FLUTUANTE - Ponto flutuante de x tamanho em bits
     - CARACTERE - Caractere
     - BOOLEANO - Booleano
     - FRASE - cadeia de caractere de x tamanho máximo de caracteres
     - *tipo_do vetor* *identificador_do_vetor*[tamanho] - Arranjos unidimencionais de qualquer tipo
     

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
   1. Coerção:
      - A linguagem prevê coerção autômatica entre o tipo INTEIRO e FLUTUANTE. Onde, se um número do tipo ponto flutuante for atribuído a uma variável do tipo inteiro, o valor da variável será apenas a parte inteira do ponto flutuando e na forma de um inteiro se atribuído a um ponto flutuante, a parte  inteira será o número e a parte decimal será zero.

1. Variáveis:
   1. Declaração:
      1. A declaração da variável tem a seguinte regra geral:
         ```
         TIPO identificador_da_variável;
         
         ```
   1. Iniciação Padrão:
      1. Pode ser feita junto da declaração da seguinte forma:
         ```
         
         TIPO identificador_da_variável = valor_do_tipo;
         
         ```
       1. Enquanto não tiver um valor atribuído a uma variável, ela terá um valor inicial padrão como se segue:
          - INTEIRO: iniciado com valor zero(0);
          - FLUTUANTE: iniciado com valor zero(0.0);
          - CARACTERE: iniciado com valor " " (espaço em branco, 32 no código ASCII);
          - BOOLEANO: iniciado com valor FALSE;
          - FRASE:  iniciado com o valor "" (cadeia de caracteres vazia);
          - *VETOR*: iniciado com o valor padrão do tipo no qual foi definido.
    1. Escopo:
       1. Na BRlanguege, todas as variáveis são globais, logo vistas em todo o programa.
1. Operadores:
   - Temos os seguintes operadores na linguagem:    
      **Aritméticos:**
      
      |Operador|Operação|
      | :---: | :---: |
      | \+ | adição |
      | \- | subtração |
      |\*| multiplicação |
      |\/| divisão |
      |\-| negativo unário |
      
      **Relacionais:**
      
      |Operador|Operação|
      | :---: | :---: |
      | \> | maior que |
      | \< | menor que |
      | \= | igual |
      | \!= | diferente de |
      | \>= | maior ou igual |
      | \<= | memor ou igual |
      
      **Lógicos:**
      
      |Operador|Operação|
      | :---: | :---: |
      | VERDADE | verdadeiro |
      | FALSO | falso |
      | NAO | negação |
      | E | conjunção |
      | OU | disjunção |
      
      **Concatenção de Cadeias de Caracteres:**
      
      |Operador|Operação|
      | :---: | :---: |
      | +++ | concatenação |
      
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
