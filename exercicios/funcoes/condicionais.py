#Exercicio 1
def fizz_buzz(numero:int):
    if numero % 3 == 0 and numero % 5 == 0:
            return "fizzbuzz"
    elif numero % 3 == 0:
            return "fizz"
    elif numero % 5 == 0:
        return "buzz"
    else:
         return numero
    
#Exercicio 2
def verificar_maioridade(idade:int):
      if idade < 18:
        return "Menor de idade"
      else:
           return "Maior de idade"
      
#Exercicio 3
def verificar_paridade(numero:int) -> bool:
      if numero % 2 == 0:
        return "É par"
      else:
           return "Não é par"
      
#Exercicio 4
def classificar_numero(numero:int) -> bool:
      if numero == 0:
        return "Zero"
      elif numero < 0:
        return "Número negativo"
      else:
           return "Número positivo"
      
#Exercicio 5
def calcular_resultado(nota1:float, nota2:float):
      if (nota1+nota2) / 2 > 12:
        return "Aprovado"
      else:
        return "Reprovado"



if __name__ == '__main__':

    teste = fizz_buzz(27)
    print(f"1 = {teste}")
    idade = verificar_maioridade(17)
    print(f"2 = {idade}")
    paridade = verificar_paridade(20)
    print(f"3 = {paridade}")
    numero = classificar_numero(0)
    print(f"4 = {numero}")
    resultado = calcular_resultado(8.0,6.0)
    print(f"5 = {resultado}")