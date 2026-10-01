class Calculadora:
    
    historico = []
        
    def __init__(self):
        
        self.historico = []
                
    def somar(self, a, b):
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        return resultado
        
    def subtrair(self, a, b):
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        return resultado
        
    def mostrar_historico(self):
        for operacao in self.historico:
            print(operacao)
        
calculadora = Calculadora()

print(f"Resultado: {calculadora.somar(5,3)}")
print(f"Resultado: {calculadora.subtrair(10,4)}")
print(f"Resultado: {calculadora.somar(7,2)}")
print(f"\nHistórico:")
calculadora.mostrar_historico()
