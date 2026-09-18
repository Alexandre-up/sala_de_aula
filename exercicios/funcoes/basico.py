#Exercicio 1
def formatar_saudacao(nome:str, cidade:str):
    return f"Olá {nome}, seja bem vinda a {cidade}!"

#Exercicio 2
def calcular_perimetro(largura:float, altura:float) -> float:
    perimetro = 2* (largura + altura)
    return perimetro

#Exercicio 3
def fahrenheit_para_celsius(temp_f) -> float:
    conversao = (temp_f - 32) * (5 / 9)
    return conversao

#Exercicio 4
def calcular_gorjeta_por_pessoa(conta:float, porcetagem_gorjeta:float, pessoas:int):
    gorjeta = (conta * (porcetagem_gorjeta/100) / pessoas)
    return gorjeta

#Exercicio 5
def resumo_circulo(raio) -> float:
    area = 3.14159 * raio**2
    return area

#Exercicio 6
def resumo_juros_compostos(capital:float, taxa:float, anos:int) -> float:
    montante = capital * (1+taxa/100)**anos
    return montante

#Exercicio 7
def metricas_cilindro(raio, altura) -> float:
    return 3.14159 * raio**2 * altura, 2 * 3.14159 * raio * (raio + altura)

#Exercicio 8
def gerar_item_fatura(nome_item:str, preco:float, porcetagem_desconto:float):
    desconto = preco * porcetagem_desconto / 100
    preco_final = preco - desconto
    return nome_item, preco_final, desconto

#Exercicio 9
def resumo_emprestimo(capital:float, taxa_anual:float, anos):
    taxa_mensal = taxa_anual * 0.0421505
    meses = anos * 12
    total = capital * (1+taxa_mensal/100)**meses
    parcela = total / meses
    return capital, parcela, total


if __name__ == '__main__':

    print("EXERCICIOS===========================================\n\n")
    saudacao = formatar_saudacao("Alice", "Porto Alegre")
    print(f"1 = {saudacao}")
    perimetro = calcular_perimetro(altura=10, largura=5)
    print(f"2 = {perimetro}")
    conversao = fahrenheit_para_celsius(68)
    print(f"3 = {conversao}")
    gorjeta = calcular_gorjeta_por_pessoa(100.0, 15, 3)
    print(f"4 = {gorjeta}")
    area = resumo_circulo(3.0)
    print(f"5 = Um círculo com raio 3.0 tem uma área de {area:.2f}")
    montante = resumo_juros_compostos(1000.0, 5.0, 3)
    print(f"6 = Após 3 anos, R$ 1000.00 cresce para R$ {montante:.2f}")
    volume, area = metricas_cilindro(2.0, 5.0)
    print(f"7 = Volume do Cilindro: {volume:.2f} | Área de Superfície: {area:.2f}")
    nome_item, preco_final, desconto = gerar_item_fatura('Teclado', 80.00, 15.0)
    print(f"8 = Item: {nome_item} | Preço Final: R$ {preco_final} (Você economizou R$ {desconto})")
    capital, parcela, total = resumo_emprestimo(10000.00, 6.0, 3.0)
    print(f"9 = Empréstimo: R$ {capital:.2f} | Parcela Mensal: R$ {parcela:.2f} | Total: R$ {total:.2f}")
    print("=====================================================")