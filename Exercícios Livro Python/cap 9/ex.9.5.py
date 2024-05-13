def ler_arquivo(nome):
    try:
        with open(nome) as f:
            print(f.read())
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except IOError:
        print("Erro ao abrir o arquivo.")


ler_arquivo('arquivo.txt')