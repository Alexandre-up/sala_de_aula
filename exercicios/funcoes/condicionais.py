#Exercício 1
def fizz_buzz(numero:int):
    if numero % 3 == 0 and numero % 5 == 0:
            return "fizzbuzz"
    elif numero % 3 == 0:
            return "fizz"
    elif numero % 5 == 0:
        return "buzz"
    else:
         return numero
    
#Exercício 2
def verificar_maioridade(idade:int):
      if idade < 18:
        return "Menor de idade"
      else:
           return "Maior de idade"
      
#Exercício 3
def verificar_paridade(numero:int) -> bool:
      if numero % 2 == 0:
        return "É par"
      else:
           return "Não é par"
      
#Exercício 4
def classificar_numero(numero:int) -> bool:
      if numero == 0:
        return "Zero"
      elif numero < 0:
        return "Número negativo"
      else:
           return "Número positivo"
      
#Exercício 5
def calcular_resultado(nota1:float, nota2:float):
      media = (nota1+nota2) / 2
      if media >= 7.0:
        return "Aprovado"
      else:
        return "Reprovado"

#Exercício 6
def maior_de_dois(a:int, b:int) -> float:
      if a < b:
        return "O segundo é maior"
      elif a > b:
              return "O primeiro é maior"
      else:
        return "São iguais"

#Exercício 7
def calcular_desconto(valor_compra:float, cliente_vip:str) -> bool:
    if (cliente_vip == True) or (valor_compra > 200):
      desconto = 0.15
    else:
        desconto = 0.05
    valor_final = valor_compra * (1 - desconto)
    return f"Valor final: R$ {valor_final:.2f}"

#Exercício 8
def conceito_nota(nota:int) -> float:
      if nota >= 9.0:
        return "A"
      elif nota >= 7.0:
        return "B"
      elif nota >= 5.0:
        return "C"
      else:
        return "F"
      
#Exercício 9
def tipo_triangulo(a:float, b:float, c:float):
    if (a+b > c) and (b+c >a) and (a+c >b):
        if a != b != c:
            return "Escaleno"
        elif a == b != c:
            return "Isóceles"
        elif a == b == c:
            return "Equilátero"
        else:
            return "Não é Triângulo"     
        
#Exercício 10
def calcular_imposto(salario:float):
    if salario <= 2000.00:
        return 0.0
    elif salario <= 4000.00:
      return (salario - 2000.00) * 0.10
    else:
        return 200.00 + (salario - 4000.00) * 0.20

#Exercício 11
def validador_bissexto(ano:int):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False
    

if __name__ == '__main__':

    print("\n=> EXERCICIOS <======================================\n")
    teste = fizz_buzz(27)
    print(f"1 → {teste}")
    idade = verificar_maioridade(17)
    print(f"2 → {idade}")
    paridade = verificar_paridade(23)
    print(f"3 → {paridade}")
    numero = classificar_numero(0)
    print(f"4 → {numero}")
    media = calcular_resultado(8.5,6.5)
    print(f"5 → {media}")
    numero = maior_de_dois(8.5,8.5)
    print(f"6 → {numero}")
    desconto = calcular_desconto(100.0, False)
    print(f"7 → {desconto}")
    conceito = conceito_nota(8.9)
    print(f'8 → Conceito "{conceito}"')
    triangulo = tipo_triangulo(6,7,9)
    print(f"9 → {triangulo}")
    imposto1 = calcular_imposto(1800.00)
    imposto2 = calcular_imposto(3000.00)
    imposto3 = calcular_imposto(5000.00)
    print(f"10 → 1800 = {imposto1} | 3000 = {imposto2} | 5000 = {imposto3}")
    bissexto1 = validador_bissexto(2024)
    bissexto2 = validador_bissexto(1900)
    bissexto3 = validador_bissexto(2000)
    print(f"11 → Ano 2024 = {bissexto1} | Ano 1900 = {bissexto2} | Ano 2000 = {bissexto3}")
    print("\n=====================================================")