import baralho

deck = baralho.cria('maco')

mao_jog1 = baralho.distribui(deck, 2)
mao_jog2 = baralho.distribui(deck, 2)


mesa = baralho.distribui(deck, 5)


print("Jogador 1", mao_jog1)

print("mesa:", mesa)

print("Jogador 2", mao_jog2)