from Pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def aumentar_salario (self, aumento):
        self.salario += self.salario * aumento / 100

    def mostrar_dados(self):
        print(f"{self.nome} tem {self.idade} anos e recebe R${self.salario:.2f} por mês.")

    