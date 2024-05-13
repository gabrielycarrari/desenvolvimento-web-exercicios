from Circulo import Circulo

class Cilindro(Circulo):
    def __init__(self, raio, altura):
        super().__init__(raio)
        self.altura = altura

    def volume(self):
        return self.area() * self.altura
    
    