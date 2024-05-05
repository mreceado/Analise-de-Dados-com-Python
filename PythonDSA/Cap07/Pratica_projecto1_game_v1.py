# Projecto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

    if name == 'nt':
        _ = system('cls')


# Função
def game():

    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo: \n")

    # Define a lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    # Usa list comprehension para preencher os tracejados de acordo com a qtd de caracteres da palavra
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Lista para as letras erradas
    letras_erradas = []
u
    # Loop enquanto número de chances for maior que zero
    while chances > 0:

        # Print
        print(" ".join(letras_descobertas)) # retira as virgulas e espaços e junta os underscores
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional
        if tentativa in palavra:     # Caso a letra faça parte da palavra então
            index = 0                # index vai percorrer os underscores 
            for letra in palavra:    # percorre a palavra 
                if tentativa == letra:   # se a 
                    letras_descobertas[index] = letra    # preenche os indices dos tracejados com a 
                index += 1                               # respecriva letra e incrementa o index
        else:
            chances -= 1  # caso a letra digitada não faça parte da palavra então decrementa as chances
            letras_erradas.append(tentativa)  # acrescenta a letra à lista de letras erradas

        # passa p/ essa condição caso os espaços estejam todos preenchidos ou a chance seja igual a zero
        if "_" not in letras_descobertas:   # caso não tenha mais undercores quer dizer que todas as
            print("\nVocê venceu, a palavra era:", palavra)  # letras foram preenchidas c/ sucesso
            break                                            # emite a mensagem e termina o programa

    # se ainda houver mais underscores por se preencher, então quer dizer que os espaços não foram 
    if "_" in letras_descobertas:   # todos preenchidos c/ sucesso 
        print("\nVocê perdeu, a palavra era:", palavra)
        

# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :) \n")
            