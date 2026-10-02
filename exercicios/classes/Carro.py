class Carro:

    marca = ""
    modelo = ""
    ligado = ""
    
    def __init__(self, marca:str, modelo:str, ligado=False):
    
        self.marca = marca
        self.modelo = modelo
        self.ligado = ligado
        
    def ligar(self):
        self.ligado = True
        #print(f"Ligado: {carro.ligado} → O carro foi ligado.")
   
    def desligar(self):
        self.ligado = False
        #print(f"Ligado: {carro.ligado} → O carro foi desligado.")
        
carro = Carro("Volkswagen", "Gol GTi")
print(f"Carro → Marca: {carro.marca} → Modelo: {carro.modelo}")

carro.ligar()
print(f"Ligado: {carro.ligado} → O carro foi ligado.")

carro.desligar()
print(f"Ligado: {carro.ligado} → O carro foi desligado.")

#print(carro.ligado)

#print(carro.desligado)
    