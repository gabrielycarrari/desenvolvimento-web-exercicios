class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def mostrar_dados(self):
        return f"{self.numerador}/{self.denominador}"
    
    def multiplicar(self, segunda_fracao):
        return Fracao(self.numerador * segunda_fracao.numerador, self.denominador * segunda_fracao.denominador)