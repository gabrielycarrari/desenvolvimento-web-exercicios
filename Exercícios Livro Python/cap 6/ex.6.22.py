import random

alfabeto = "abcdefghijklmnopqrstuvwxyz"
nome = "gabriely"
sorteados = ""

qtd_sorteios = 0

while set(nome) != set(sorteados):
    letra = random.choice(alfabeto)
    if letra in nome and letra not in sorteados:
        sorteados += letra
    qtd_sorteios += 1

print(f"As letras do nome {nome} foi sorteado em {qtd_sorteios} tentativas.")