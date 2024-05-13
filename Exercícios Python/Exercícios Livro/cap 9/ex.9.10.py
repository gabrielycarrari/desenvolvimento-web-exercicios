def importar_modulo(modulo):
    try:
        __import__(modulo)
        print(f'Módulo {modulo} importado com sucesso.')
    except ModuleNotFoundError:
        print(f'Módulo {modulo} não encontrado.')


importar_modulo('math')
importar_modulo('matematica')