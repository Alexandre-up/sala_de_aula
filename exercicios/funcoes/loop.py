#Exercício
def dobrar(numeros:[]):
    for numero in numeros:
        numero = numero * 2
        print(numero, end=" ")

#Exercício 1
def filtrar_pares(numeros:list):
    pares = [] # ou list()
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares
    
#Exercício 2
def contar_negativos(numeros:list):
        count = 0
        for numero in numeros:
             if numero < 0:
                count += 1
        return count

#Exercício 3
def somar_maiores_que(numeros:list, limite):
    soma = 0
    for numero in numeros:
        if numero > limite:
            soma += numero
    return soma

#Exercício 4
def zerar_negativos(numeros:list):
    aux = numeros.copy()
    for numero in numeros:
        if numero < 0:
            indice = numeros.index(numero)
            aux[indice] = 0
    return aux

#Exercício 5
def contem_valor(lista:list, alvo):
    index = 0
    while(index < len(lista)):
        if lista[index] == alvo:
            return True
        index =+ 1

    return False

#Exercício 6
def contar_aprovados(notas:list) -> float:
    aprovados = 0
    for nota in notas:
        if nota >= 7.0:
            aprovados += 1

    return aprovados

#Exercício 7
def filtrar_palavras_curtas(palavras:list, tamanho_maximo:int):
    filtro = []
    for palavra in palavras:
        if len(palavra) <= tamanho_maximo:
            filtro.append(palavra)
    return filtro

#Exercício 8
def separar_pares_impares(numeros:list):
    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    return f"8º → Pares: {pares} | Ímpares: {impares}"

#Exercício 9
def encontrar_extremos(numeros:list):
    menor = numeros[0]
    maior = numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
    return (menor,maior)

#Exercício 10
def simular_saque(saldo_inicial:float, saques:list):
    saldo = saldo_inicial
    i = 0
    while i < len(saques):
        saque = saques[i]
        if saque <= saldo:
            saldo -= saque
        i += 1
    return saldo

#Exercício 11
def remover_duplicados(lista):
    resultado = []
    for elemento in  lista:
        if elemento not in resultado:
            resultado.append(elemento)

    return resultado
    
#Exercício 12
def media_positivos(numeros:list):
    soma = 0
    quantidade = 0
    for numero in numeros:
        if numero > 0:
            soma += numero
            quantidade += 1            
    if quantidade == 0:
        return 0.0        
    return soma / quantidade
    
#Exercício 13
def validar_senhas(lista_senhas:list[str]):
    senhas_validas = []
    for senha in lista_senhas:
        if len(senha) >= 8:
            senhas_validas.append(senha)
    return senhas_validas
    
#Exercício 14
def primeiro_impar(numeros):
    i = 0
    while i < len(numeros):
        if numeros[i] % 2 != 0:
            return numeros[i]
        i += 1
    return None
    
#Exercício 15
def contar_ocorrencias(lista:list, alvo):
    quant = 0
    for obj in lista:
        if obj == alvo:
            quant += 1
    return quant
    
#ExercÍcio 16
def estritamente_crescente(palavras:list):
    i = 1
    
    while i < len(palavras):
        if len(palavras[i]) <= len(palavras[i-1]):
            return False            
        i += 1        
    return True

#Exercício 17
def mover_zeros_final(numeros:list):
    zeros = []
    
    for numero in numeros:
        if numero != 0:
            zeros.append(numero)
            
    for numero in numeros:
        if numero == 0:
            zeros.append(numero)
    
    return zeros
    
#Exercício 18
def processar_fila(clientes:list[tuple]):
    preferenciais = []
    demais = []
    
    for nome, idade in clientes:
        if idade >= 60:
            preferenciais.append(nome)
        else:
            demais.append(nome)
            
    return preferenciais + demais
    
#Exercício 19
def encontrar_picos(numeros:list):
    picos = []
    i = 1
    
    while i < len(numeros) - 1:
        if numeros[i] > numeros[i-1] and numeros[i] > numeros [i+1]:
            picos.append(numeros[i])
            
        i += 1
        
    return picos
    
#Exercício 20
def validar_extrato(saldo_inicial:float, transacoes:list):
    saldo = saldo_inicial
    i = 0
    
    while i < len(transacoes):
        saldo += transacoes[i]
        
        if saldo < 0:
            return f"Extato Inválido: Saldo Negativo na Posição {i}"
            
        i += 1
        
    return f"Extrato Válido: Saldo Final {saldo:.2f}"


if __name__ == '__main__':

    print("\n=> EXERCICIOS <======================================\n")
    print("-> → ", end="")
    dobro = dobrar([1,2,3,4,5])
    numeros_pares = filtrar_pares([1,2,3,4,5,6])
    print(f"\n1º → {numeros_pares}")
    n_negativos = contar_negativos([-3,-2,-1,0,1,2,3,])
    print(f"2º → [{n_negativos}]")
    limite = somar_maiores_que([10, 5, 20, 3, 15], 8)
    print(f"3º → [{limite}]")
    zerar = zerar_negativos([-3,-2,-1,0,1,2,3])
    print(f"4º → {zerar}")
    valor = contem_valor(["maçã", "banana", "uva"], "banana")
    print(f"5º → [{valor}]")
    aprovados = contar_aprovados([8.5,5.0,7.0,6.5,9.0])
    print(f"6º → [{aprovados}]")
    palavras = filtrar_palavras_curtas(["sol", "computador", "python", "mar"],6)
    print(f"7º → {palavras}")
    separar = separar_pares_impares([1,2,3,4,5,6,7,8])
    print(separar)
    extremos = encontrar_extremos([14,2,35,-4,20])
    print(f"9º → {extremos}")
    saque = simular_saque(200,[50,100,80,30])
    print(f"10º → Saldo: [R${saque},00]")
    duplicados = remover_duplicados([1, 3, 2, 3, 1, 4, 2])
    print(f"11º → Duplicados: {duplicados}")
    media = media_positivos([-5, 10, -2, 20, 30])
    print(f"12º → {media}")
    validas = validar_senhas(["12345", "senha1234", "admin", "python2026"])
    print(f"13º → {validas}")
    primeiro = primeiro_impar([2,4,6,7,9,10,11,13])
    print(f"14º → [{primeiro}]")
    contar = contar_ocorrencias(["a","b","a","c","a"], "a")
    print(f"15º → [{contar}]")
    estrito1 = estritamente_crescente(["lá", "lua", "cinema", "computador"])
    estrito2 = estritamente_crescente(["palito", "geringonça", "lápis", "lâmpada"])
    print(f"16º → {estrito1} | {estrito2}")
    mover = mover_zeros_final([0,1,0,3,12,0,5])
    print(f"17º → {mover}")
    fila = processar_fila([("Ana",25), ("Bento",67), ("Carla",18), ("Daniel",72)])
    print(f"18º → {fila}")
    resultado = encontrar_picos([1,5,2,6,3,1,8,4])
    print(f"19º → {resultado}\n")
    print(f"20º → Saldo1: {validar_extrato(100,[-50,-60,20])}")    
    print(f"    → Saldo2: {validar_extrato(50,[30,-40,-20,100])}")
    print("\n=====================================================")