def contagemRegressiva(num: int):
    if num >= 0:
        print(num)
        contagemRegressiva(num-1)
    else:
        print("Contagem regressiva finalizada!")


contagemRegressiva(5)