semaforo = input("Digite a cor do semáforo: ")

match semaforo.lower():
    case 'verde':
        print("Prossiga.")
    case 'amarelo':
        print("Prepare-se para parar.")
    case 'vermelho':
        print("Pare.")
    case _:
        print("Cor inválida.")