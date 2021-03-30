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
   
   VAZIO FUNCAO PRINCIPAL(){
      RETORNE ;
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
     | FLUTUANTE | PRINCIPAL | OU_SE | FALSO |
     | CARACTERE | LER | SENAO | NAO |
     | BOOLEANO | IMPRIMIR | FAZ | E |
     | FRASE | RETORNE | ENQUANTO | OU |
     |VAZIO||ITERADOR||
     
1. Especificação de Tipos:
   - A linguagem é tipada estaticamente, o que significa que toda variavél precisa indicar o seu tipo ao ser declarada e esse tipo fica inculado a varíavel durante toda a sua vida;
   - Lista de tipos definidos em BRLanguage:
     - INTEIRO - Inteiro de x tamanho em bits
     - FLUTUANTE - Ponto flutuante de x tamanho em bits
     - CARACTERE - Caractere
     - BOOLEANO - Booleano
     - FRASE - cadeia de caractere de x tamanho máximo de caracteres
     - *tipo_do vetor* *identificador_do_vetor*[tamanho] - Arranjos unidimencionais de qualquer tipo
     - VAZIO - Tipo de dado que representa função sem retorno.
     

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
      | \== | igual |
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
      
    1. Precedência e Associatividade:
       - Conforme a tabela abaixo, da ordem da mais alta para a mais baixa vemos a Precedência e os operadores segue a Associatividade espeficificada:
          |Operador|Associatividade|
          | :---: | :---: |
          | NAO | direita para esquerda |
          |\- (negativo unário)| direita para esquerda |
          | \* \/ | esquerda para direita |
          | \+ \- | esquerda para direita |
          | \< \<= \> \>= | esquerda para direita |
          | \== \!= | esquerda para direita |
          | E | esquerda para direita |
          | OU | esquerda para direita |
        - Podemos utilizar parênteses para alterar a precedência dos operadores acima.

1. Instruções:
   1. Estrutura condicional de uma e duas vias:
      | Estrutura | Comando em Brl |
      | :---: | :---: |
      | if | SE |
      | if \/ else | SE \/ SENAO |
      | if \/ elseif \/ else | SE \/ MAS_SE \/ SENAO |
      - A instrução SE controla a fluxo condicional. O bloco da instrução SE é executado se o valor da expressão for diferente de zero. Temos duas sintaxes para essa estrutura:
      ```
      
      SE(expressao_logica){
         lista_de_comandos;
      };
      
      ```
      ou
      ```
      
      SE(expressao_logica){
         lista_de_comandos_1;
      }
      ENTAO(espressao_logica){
         lista_de_comandos_2;
      };
      ```
      - Usamos uma expressao lógica para controlar essa estrutura condicional.
      - Se uma forma mais abrangente de verificação for necessária temos o SE's aninhados, utilizando o comando SENAO.
      ```
      
      SE(expressao_logica){
         lista_de_comandos_1;
      }
      SENAO(expressao_logica){
         lista_de_comandos_2;
      }
      ENTAO(espressao_logica){
         lista_de_comandos_3;
      };
      ```
   1. Estrutura iterativa com controle lógico:
      | Estrutura | Comando em Brl |
      | :---: | :---: |
      | while | ENQUANTO | 
      | do while | FAZER ENQUANTO |
      - A estrutura ENQUANTO permite que se repita uma instrução até que seja verificado que uma expressão é falsa.
      Sintaxe:
      ```
      ENQUANTO(expressao_logica){
         lista_de_comandos;
      };
      
      ```
      - A estrutura FAZ ENQUANTO permite que se repita uma instrução pelo menos uma vez, mesmo que a expressão seja falsa.
      
      Sintaxe:
      ```
      
      FAZER{
         lista_de_comandos;
      }ENQUANTO(expressao_logica);
      
      ```
   1. Estrutura iterativa controlada por contador:
      | Estrutura | Comando em Brl |
      | :---: | :---: |
      | for | ITERADOR |
      - A estrutura ITERADOR permite que seja repetida uma instrução composta por um número específico de vezes. O corpo da estrutura é executado zero ou mais vezes até que a condição seja verificada como falsa.
      
      Sintaxe:
      ```
      
      ITERADOR(inicialização, condicao, incremento){
         lista_de_comandos;
      };
      
      ```
   1. Entrada e Saida
      | Entrada | Saida |
      | :---: | :---: |
      |LER|IMPRIMIR|
      - IMPRIMIR é a instrução de escrita na tela, recebe como parâmetro um dos tipos da linguagem , permite a formatação atravez da concatenação de cadeia de caracteres e variáveis.

      Sintaxe:
      ```

      IMPRIMIR(frase_para_imprimir_na_tela);

      ```
      - LER é a instrução que lê algo, deve receber o tipo a ser lido e sua variável para referência.
      ```

      LER(TIPO, variavel_para_referencia);

      ```
1. Atribuição:
   A atribuição é feita com operador "=", com a associatividade da direita para a esquerda, sempre.

   Exemplo:
   ```

   a = b;

   ```
   *o valor da variável b está agora sendo atribuído para a*

1. Funções:
   - Na BRLanguage, temos a função PRINCIPAL e ela é obrigatória pois é por ela que o compilador começa sua execução.
   - As funções devem ser definidas antes de serem chamadas.
   - A passagem de parâmetro ocorre por valor na liguagem.
   - Para o retorno de funções, utilizamos o operador RETORNE na última linha do escopo da função 
   - A definição segue a regra abaixo:
   ```

   TIPO_DE_RETORNO nome_da_função(parametros){
      comandos;
      ...
      ...
      ...
      RETORNE TIPO_DE_RETORNO

   }

   ```
1. Exemplos:
   - Alô Mundo:
   ```

   VAZIO PRINCIPAL(){
      IMPRIMIR("Alô Mundo!");
      RETORNE ;
   }

   ```

   - Fibonacci:
   ```

   VAZIO fibonacci(INTEIRO limite){
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
            IMPRIMIR(tres +++ " ");
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

   ```

   - Shell Sort
   ```

   INTEIRO shell(INTEIRO array[], INTEIRO tamanho){
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

   VAZIO PRINCIPAL(){
      INTEIRO vetor[10];
      INTEIRO saida[10];

      vetor = [9, 8, 3, 2, 5, 1, 4, 7, 6, 0];

      saida = shell(vetor, 10);
   }

   ```


   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   


