def verificar_palavra(palavra_secreta):
    try:
        while True:
            palavra = input('Digite a palavra secreta: ').lower()
            if not palavra.isalpha():
                raise ValueError('A palavra não pode conter números ou caracteres especiais.')
            if palavra.lower() == palavra_secreta:
                print('Você acertou!')
                break
    except ValueError as e:
        print(e)


verificar_palavra("teste")
