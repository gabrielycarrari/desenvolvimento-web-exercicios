def calcular_media(lista):
    try:
       return sum(lista)/len(lista)
    except ZeroDivisionError:
        print("Erro: A lista não pode estar vazia.")
    except TypeError: 
        print("Erro: A lista deve ter apenas elementos numéricos.")


lista = [1, 2, 3, 4, 5, 6]
print(calcular_media(lista))