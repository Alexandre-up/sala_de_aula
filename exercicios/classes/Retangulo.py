class Retangulo:
    
    base = 0.0
    altura = 0.0
    
    def __init__(self, base:float, altura:float):
        
        self.base = base
        self.altura = altura       
        
    def calcular_area(self):
        return self.base * self.altura
        
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
        
retangulo = Retangulo(10.0, 5.0)
retangulo.calcular_area()
retangulo.calcular_perimetro()
print(f"Área: {retangulo.calcular_area()} | Perímetro: {retangulo.calcular_perimetro()}")