class Relogio:
    
    hora = 0
    minuto = 0
    segundo = 0
    
    def __init__(self, hora:int, minuto:int, segundo:int):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        
    def avancar_tempo(self, segundos):
        self.segundo += segundos
        
        self.minuto += self.segundo // 60
        self.segundo = self.segundo % 60
        
        self.hora += self.minuto // 60
        self.minuto = self.minuto % 60
        
        self.hora = self.hora % 24
        

relogio = Relogio(23,59,59)
relogio.avancar_tempo(1201)
print(f"Horário: {relogio.hora:02d}:{relogio.minuto:02d}:{relogio.segundo:02d}")


        