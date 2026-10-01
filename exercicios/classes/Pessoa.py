class Pessoa:
    
    nome: ""
    cidade: ""
    
    def __init__(self, nome:str, cidade:str):
        
        self.nome = nome
        self.cidade = cidade        
        
    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e moro em {self.cidade}.")
        
pessoa = Pessoa("Alexandre", "Porto Alegre")
pessoa.apresentar()