class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome.upper()
        self.idade = idade

    @property
    def idade(self) -> int:
        return self.__idade
    
    @idade.setter
    def idade(self, valor: int):
        if 0 <= valor <= 120:
            self.__idade = valor
        else:
            raise Exception(f"Idade {valor} é inválida. Deve estar entre 0 e 120.")
    
    def falar(self, mensagem):
        print(f"{self.nome} falou '{mensagem}'.")
    
        