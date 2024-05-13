def transformar_lista(lista: list[int], operacao):
    lista_processada = []

    for num in lista:
        num_processado = por_extenso(num)
        lista_processada.append(num_processado)
    
    return lista_processada

def por_extenso(num: int):
    match num:
        case 1:
            return "Um"
        case 2:
            return "Dois"
        case 3:
            return "Três"
        case 4:
            return "Quatro"
        case 5:
            return "Cinco"
        case 6:
            return "Seis"
        case 7:
            return "Sete"
        case 8:
            return "Oito"
        case 9:
            return "Nove"
        case 0:
            return "Zero"
        case _:
            return "Não encontrado"
        
    
numeros = [1, 2, 3, 4, 5]
resultado = transformar_lista(numeros, por_extenso)
print(resultado)