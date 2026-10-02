class Cachorro:
    
    nome = ""
    raca = ""
    idade = 0
    
    def __init__(self, nome:str, raca:str, idade:int):
        
        self.nome = nome
        self.raca = raca
        self.idade = idade
        
    def latir(self):
        print(f"Au au! O {self.nome} está latindo.")
        
cachorro = Cachorro("Rex", "Labrador", 5)
cachorro.latir()
