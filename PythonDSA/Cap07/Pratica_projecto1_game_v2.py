# Projecto 1 - Desenvolvimento de Game em Linguagem Python - Versão 2

import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

    if name == 'nt':
        _ = system('cls')



# Função que desenha a forca na tela
def display_hangman(chances):

    # Lista de estágios da forca
    stages = [ # estágio 6 (final)
                """
                ----------
                |        |
                |        O
                |      \\|/
                |        |
                |       /\\
                -
                """,

                # estágio 5
                """
                ----------
                |        |
                |        O
                |      \\|/
                |        |
                |       /
                -
                """, 

                # estágio 4
                """
                ----------
                |        |
                |        O
                |      \\|/
                |        |
                |       
                -
                """, 

                # estágio 3
                """
                ----------
                |        |
                |        O
                |      \\|
                |        |
                |       
                -
                """, 

                # estágio 2
                """
                ----------
                |        |
                |        O
                |        |
                |        |
                |       
                -
                """, 

                # estágio 1
                """
                ----------
                |        |
                |        O
                |      
                |        
                |       
                -
                """, 

                # estágio 0
                """
                ----------
                |        |
                |        
                |      
                |        
                |       
                -
                """

    ]

    return stages[chances]



# Função
def game():

    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo: \n")

    # Define a lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # Escolhe randomicamente (aleatoriamente) uma palavra
    palavra = random.choice(palavras)

    # Usa list comprehension para preencher os tracejados de acordo com a qtd de caracteres da palavra
    lista_letras_palavras = [letra for letra in palavra]

    # Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)

    # Número de chances
    chances = 6

    # Lista para as letras erradas
    letras_tentativas = []

    # Loop enquanto número de chances for maior que zero
    while chances > 0:

        # Print
        print(display_hangman(chances)) # chama as strings com o desenho da forca, a partir da posição 6, que é o estágio 0 da string
        print(" ".join(tabuleiro))  
        print(palavras) 
        print(palavra) 
        print(lista_letras_palavras)
        print(chances)
        print("\n")

        # Tentativas
        tentativa = input("\nDigite uma letra: ")

        # Condicional 
        if tentativa in letras_tentativas:     # Caso já tenha inserido essa letra então
            print("Você já tentou essa letra, escolha outra!")  # imprime esta mensagem 
            continue  # devolve o controle para o while
            
            # Lista de letras já digitadas
            letras_tentativas.append(tentativa) # acrescenta a letra à lista de tentativas

            # Condicional - Se letra digitada faz parte da palavra escolhida aleatoriamente
        if tentativa in lista_letras_palavras:

            print("Você acertou a letra!")

            # Loop - o indice vai percorrer o tamanho da lista da palavra seleccionada
            for indice in range(len(lista_letras_palavras)):

                # Condicional - para cada posição (indice) da palavra 
                if lista_letras_palavras[indice] == tentativa:   # analisa se as letras contidas nos indices são iguais a letra digitada
                    tabuleiro[indice] = tentativa   # se sim, então preenche os respectivos espaços do tabuleiro (underscores) com a letra digitada
                
            # Se todos os espaços foram preenchidos, o jogo acabou
            if "_" not in tabuleiro:
                print("\nVocê venceu! a palavra era: {}.".format(palavra))
                break
        else: # Se letra digitada não faz parte da palavra escolhida aleatoriamente
            print("Ops. Essa letra não está na palavra!")  # imprime a mensagem 
            chances -= 1   # e decrementa

    # Condicional
    if "_" in tabuleiro:
        print("\nVocê perdeu! A palavra era: {}.".format(palavra))

# Bloco main
if __name__ == "__main__":
            game()
            print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")