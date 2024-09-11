def inicializar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True
    # Verificar colunas
    for col in range(3):
        if [tabuleiro[row][col] for row in range(3)].count(jogador) == 3:
            return True
    # Verificar diagonais
    if [tabuleiro[i][i] for i in range(3)].count(jogador) == 3:
        return True
    if [tabuleiro[i][2 - i] for i in range(3)].count(jogador) == 3:
        return True
    return False

def verificar_empate(tabuleiro):
    return all(cell != " " for row in tabuleiro for cell in row)

def fazer_jogada(tabuleiro, jogador, linha, coluna):
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
        return True
    return False

def main():
    tabuleiro = inicializar_tabuleiro()
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, faça sua jogada!")

        try:
            linha = int(input("Escolha a linha (0, 1, 2): "))
            coluna = int(input("Escolha a coluna (0, 1, 2): "))
        except ValueError:
            print("Entrada inválida. Digite números inteiros.")
            continue

        if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
            print("Posição inválida. Escolha entre 0, 1 ou 2.")
            continue

        if fazer_jogada(tabuleiro, jogador_atual, linha, coluna):
            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                break

            if verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print("Empate!")
                break

            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("A célula já está ocupada. Tente novamente.")

if __name__ == "__main__":
    main()
