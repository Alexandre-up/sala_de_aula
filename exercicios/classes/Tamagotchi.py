class Tamagotchi:
    
    nome = ""
    fome = 0
    energia = 0
    
    def __init__(self, nome:str, fome:int, energia:int):
        
        self.nome = nome
        self.fome = fome
        self.energia = energia        
        
    def comer(self):
        self.fome -= 20                     
        self.energia += 10
        
        if self.fome < 0:
            self.fome = 0
            
        if self.energia > 100:
            self.energia = 100
            
    def brincar(self):            
        self.fome += 20
        self.energia -= 10
            
        if self.fome > 100:
           self.fome = 100            
        
tamagotchi = Tamagotchi("Bidu", 50, 50)
print(f"Nome → {tamagotchi.nome}")
print(f"Fome: {tamagotchi.fome}")
print(f"Energia: {tamagotchi.energia}")

tamagotchi.comer()
print(f"\nDepois de comer:")
print(f"Fome: {tamagotchi.fome}")
print(f"Energia: {tamagotchi.energia}")

tamagotchi.brincar()
print(f"\nDepois de brincar:")
print(f"Fome: {tamagotchi.fome}")
print(f"Energia: {tamagotchi.energia}")
