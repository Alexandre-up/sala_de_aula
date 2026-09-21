#exercicio 0
def dobrar(numeros:[]):
    for numero in numeros:
        numero = numero * 2
        print(numero)

#Exercicio 1
def filtrar_pares(numeros:list):
    pares = [] # ou list()
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares
    
#Exercicio 2
def contar_negativos(numeros:list):
        count = 0
        for numero in numeros:
             if numero < 0:
                count += 1
        return count

#Exercicio 3
def somar_maiores_que(numeros:list, limite):
    soma = 0
    for numero in numeros:
        if numero > limite:
            soma += numero
    return soma

#Exercicio 4
def zerar_negativos(numeros:list):
    aux = numeros.copy()
    for numero in numeros:
        if numero < 0:
            indice = numeros.index(numero)
            aux[indice] = 0
    return aux

#Exercicio 5
def contem_valor(lista:list, alvo):
    index = 0
    while(index < len(lista)):
        if lista[index] == alvo:
            return True
        index =+ 1

    return False

#Exercicio 6
def contar_aprovados(notas:list) -> float:
    aprovados = 0
    for nota in notas:
        if nota >= 7.0:
            aprovados += 1

    return aprovados

#Exercicio 7
def filtrar_palavras_curtas(palavras:list, tamanho_maximo:int):
    filtro = []
    for palavra in palavras:
        if len(palavra) <= tamanho_maximo:
            filtro.append(palavra)
    return filtro

#Exercicio 8
def separar_pares_impares(numeros:list):
    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    return f"8º → Pares: {pares} | Ímpares: {impares}"

#Exercicio 9
def encontrar_extremos(numeros:list):
    menor = numeros[0]
    maior = numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
    return (menor,maior)

#Exercicio 10
def simular_saque(saldo_inicial:float, saques:list):
    saldo = saldo_inicial
    i = 0
    while i < len(saques):
        saque = saques[i]
        if saque <= saldo:
            saldo -= saque
        i += 1
    return saldo



if __name__ == '__main__':

    print("\n=> EXERCICIOS <====================================\n")
    dobro = dobrar([1,2,3,4,5])   
    numeros_pares = filtrar_pares([1,2,3,4,5,6])
    print(f"1º → {numeros_pares}")
    n_negativos = contar_negativos([-3,-2,-1,0,1,2,3,])
    print(f"2º → [{n_negativos}]")
    limite = somar_maiores_que([10, 5, 20, 3, 15], 8)
    print(f"3º → [{limite}]")
    zerar = zerar_negativos([-3,-2,-1,0,1,2,3])
    print(f"4º → {zerar}")
    valor = contem_valor(["maçã", "banana", "uva"], "banana")
    print(f"5º → {valor}")
    aprovados = contar_aprovados([8.5,5.0,7.0,6.5,9.0])
    print(f"6º → [{aprovados}]")
    palavras = filtrar_palavras_curtas(["sol", "computador", "python", "mar"],6)
    print(f"7º → {palavras}")
    separar = separar_pares_impares([1,2,3,4,5,6,7,8])
    print(separar)
    extremos = encontrar_extremos([14,2,35,-4,20])
    print(f"9º → {extremos}")
    saque = simular_saque(200,[50,100,80,30])
    print(F"10º → Saldo: R${saque},00")
    print("\n===================================================")