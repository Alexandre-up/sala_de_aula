class ContaBancaria:
    
    titular = ""
    saldo = 0.0
    
    def __init__(self, titular:str, saldo=0.0):
        
        self.titular = titular
        self.saldo = saldo       
        
    def depositar(self, valor:float):
        self.saldo += valor
        
conta = ContaBancaria("Alexandre")
conta.depositar(500.0)
print(f"Titular: {conta.titular} | Saldo: R$: {conta.saldo:.2f}")