import random

pessoas=["Alice", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo", "Helena", "Igor", "Juliana"]
sorteios = {}

for p in pessoas:
    opcoes = list(set(pessoas) - set([p]) - set(sorteios.values()))
    print(opcoes)
    sorteios[p] = random.choice(opcoes)

for p, s in sorteios.items():
    print(f"{p} tirou {s}")
