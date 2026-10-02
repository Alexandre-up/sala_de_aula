class Livro:
    
    titulo = ""
    autor = ""
    paginas = 0
    
    def __init__(self, titulo:str, autor:str, paginas:int):
        
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas       
        
    def resumo(self):
        return self.titulo, self.autor, self.paginas
                    
livro = Livro("Dom Casmurro", "Machado de Assis", 256)

titulo, autor, paginas = livro.resumo()

print(
    f"\nO livro {titulo} foi escrito por"
    f"\n{autor} e possui {paginas} páginas.")