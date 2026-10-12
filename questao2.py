# Apresentação e cardápio de Pizzas para escolha
print("----------------- Bem-vindo a Pizzaria de Pablo Henrique Oliveira Rodrigues -----------------")
print("------------------------------------------Cardápio------------------------------------------")
print("---|  Tamanho  |  Pizza Salgada (PS)  |  Pizza Doce (PD)  |---")
print("---|     P     |       R$ 30.00       |     R$ 34.00      |---")
print("---|     M     |       R$ 45.00       |     R$ 48.00      |---")
print("---|     G     |       R$ 60.00       |     R$ 66.00      |---")
print("--------------------------------------------------------------------------------------------")
# Variavel acumuladora que apresentará o valor final a ser pago 
acumulador = 0.0
# Início do Loop de escolha de tipo e tamanho
while True:
    # Pergunta o tipo da pizza e, se inválido, retorna a mesma pergunta após avisar ao usuário
    sabor = str(input("Insira o sabor desejado: (PS ou PD) "))
    if sabor != "PS" and sabor != "PD":
        print("Sabor inválido. Tente novamente.")
        continue
    # Pergunta o tamanho da pizza e, se inválido, retorna a mesma pergunta após avisar ao usuário
    tamanho = str(input("Insira o tamanho desejado: "))
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente.")
        continue
    # Registro do preço e tamanho da pizza solicitada para cálculo e apresentação no resultado final
    if sabor == "PS":
        if tamanho == "P":
            preco = 30.00
            tipo = "Pizza Salgada no tamanho P"
        elif tamanho == "M":
            preco = 45.00
            tipo = "Pizza Salgada no tamanho M"
        # se o tamanho não é P, nem M, só pode ser G
        else:
            preco = 60.00
            tipo = "Pizza Salgada no tamanho G"
    # Se o sabor é diferente de PS, só pode ser PD
    else:
        if tamanho == "P":
            preco = 34.00
            tipo = "Pizza Doce no tamanho P"
        elif tamanho == "M":
            preco = 48.00
            tipo = "Pizza Doce no tamanho M"
        # se o tamanho não é P, nem M, só pode ser G
        else:
            preco = 66.00
            tipo = "Pizza Doce no tamanho G"
    # Variável acumuladora recebe a soma de si mesmo com o valor da pizza pedida, permite adições infinitas pelo usuário
    acumulador = acumulador + preco
    # Apresenta o tipo e preço da Pizza solicitada
    print(f"Você pediu uma {tipo}: R$ {preco:.2f}")
    # Pergunta se o usuário deseja mais uma pizza, se não, encerra o Loop, se sim, retorna ao passo anterior
    resposta = str(input("Você quer pedir mais alguma pizza? Sim ou Não?"))
    # Inseridas três formas de digitar não para previnir erro do usuário
    if resposta == "Não" or resposta == "N" or resposta == "n":
        break
print(f"O valor total a ser pago: R$ {acumulador:.2f}")