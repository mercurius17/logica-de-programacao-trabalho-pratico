# Mensagem de boas-vindas com nome completo
print("Bem-vindo a Madeireira de Pablo Henrique Oliveira Rodrigues!")
# Função que armazena o valor do tipo de madeira escolhida quando chamada
def escolha_tipo():
    while True:
        print("Entre com o Tipo de Madeira desejado")
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peroba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia")
        tipoMadeira = input(">> ")
        if tipoMadeira == "PIN":
            return 150.40
        elif tipoMadeira == "PER":
            return 170.20
        elif tipoMadeira == "MOG":
            return 190.90
        elif tipoMadeira == "IPE":
            return 210.10
        elif tipoMadeira == "IMB":
            return 220.70
        # Qualquer valor diferente dos listados acima, retorna escolha inválida e repete a solicitação
        else:
            print("Escolha inválida, entre com o tipo de madeira novamente")
            continue
# Função que armazena o quantidade de toras escolhida e desconto quando chamada
def qtd_toras():
    while True:
        try:
            qtdToras = float(input("Entre com a quantidade de toras por m³: "))
            # Se quantidade escolhida for maior que 2000, comunica ao usuário e repete a solicitação
            if qtdToras > 2000:
                print("Não aceitamos pedidos com essa quantidade de toras.")
                print("Por favor, entre com a quantidade novamente.")
                continue
            # Sequência de cálculo de desconto baseado na quantidade desejada
            if qtdToras < 100:
                desconto = 0 / 100      # 0% de desconto
            elif qtdToras < 500:
                desconto = 4 / 100      # 4% de desconto
            elif qtdToras < 1000:
                desconto = 9 / 100      # 9% de desconto
            else:  # Entre 1000 e 2000
                desconto = 16 / 100     # 16% de desconto
            return qtdToras, desconto
        # Em caso de preenchimento com valor não numérico, comunica o erro e repete a solicitação
        except ValueError:
            print("Valor não numérico. Por favor, entre com a quantidade novamente.")
            continue
# Função que armazena o valor do transporte escolhido quando chamada
def transporte():
    while True:
        print("Escolha o tipo de Transporte:")
        print("1 - Transporte Rodoviário - R$ 1000.00")
        print("2 - Transporte Ferroviário - R$ 2000.00")
        print("3 - Transporte Hidroviário - R$ 2500.00")
        opcao = input(">> ")
        if opcao == "1":
            return 1000.00
        elif opcao == "2":
            return 2000.00
        elif opcao == "3":
            return 2500.00
        else: # Comunica ao usuário quando inserido opção de transporte inválido
            print("Opção inválida de transporte. Tente novamente.")
            continue
# Código principal que chama as funções anteriores, realiza o cálculo do valor final e apresenta ao usuário
tipoMadeira = escolha_tipo()
qtdToras, desconto = qtd_toras()
transporte = transporte()
total = ((tipoMadeira * qtdToras) * (1 - desconto)) + transporte
print(f"Total: R$ {total:.2f}")