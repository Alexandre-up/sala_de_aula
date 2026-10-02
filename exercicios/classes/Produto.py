class Produto:
    
    nome = ""
    preco = 0.0
    
    def __init__(self, nome:str, preco:float):
        
        self.nome = nome
        self.preco = preco       
        
    def desconto(self, percentual:float):
        self.preco -= self.preco * (percentual / 100)
        
produto = Produto("Teclado", 80.0)
produto.desconto(15)
print(f"Produto: {produto.nome} | Preço: R$ {produto.preco:.2f}")
