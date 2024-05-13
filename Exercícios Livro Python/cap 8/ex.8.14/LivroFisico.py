from Livro import Livro

class LivroFisico(Livro):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor)
        self.paginas = paginas

    def mostrar_dados(self):
        print(f"O livro '{self.titulo}', escrito por {self.autor}, tem {self.paginas} páginas.")