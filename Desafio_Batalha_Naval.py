import random

# Função para criar o tabuleiro
def criar_tabuleiro():
    tabuleiro = [['~' for _ in range(5)] for _ in range(5)]
    return tabuleiro

# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

# Função para gerar as posições dos navios
def gerar_navios():
    navios = []
    while len(navios) < 3:
        linha = random.randint(0, 4)
        coluna = random.randint(0, 4)
        if (linha, coluna) not in navios:
            navios.append((linha, coluna))
    return navios

# Função para processar o movimento do jogador
def jogar():
    tabuleiro = criar_tabuleiro()
    navios = gerar_navios()
    tentativas = 0
    acertos = 0

    print("Bem-vindo ao jogo de Batalha Naval!")
    print("Tente acertar os navios! Você tem 3 navios escondidos no tabuleiro 5x5.")
    
    while acertos < 3:
        exibir_tabuleiro(tabuleiro)
        
        # Solicitar a posição de tentativa
        try:
            linha = int(input("Escolha a linha (0-4): "))
            coluna = int(input("Escolha a coluna (0-4): "))
        except ValueError:
            print("Por favor, insira números válidos para linha e coluna.")
            continue

        # Verificar se a tentativa é válida
        if linha < 0 or linha > 4 or coluna < 0 or coluna > 4:
            print("Escolha uma linha e coluna dentro do intervalo de 0 a 4.")
            continue

        # Verificar se o jogador já tentou essa posição
        if tabuleiro[linha][coluna] != '~':
            print("Você já tentou essa posição!")
            continue

        # Verificar se a posição é um navio
        if (linha, coluna) in navios:
            print("Você acertou um navio!")
            tabuleiro[linha][coluna] = 'X'  # Marcar como acerto
            acertos += 1
        else:
            print("Água!")
            tabuleiro[linha][coluna] = 'O'  # Marcar como erro
        tentativas += 1
    
    print(f"Você venceu! Total de tentativas: {tentativas}")
    exibir_tabuleiro(tabuleiro)

# Iniciar o jogo
if __name__ == "__main__":
    jogar()