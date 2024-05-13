class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_dados(self):
        print(f"O livro '{self.titulo}', escrito por {self.autor}")