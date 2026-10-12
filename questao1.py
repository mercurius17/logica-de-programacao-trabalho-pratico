# Mensagem de boas-vindas com nome completo
print("Bem-vindo! Este é o Sistema de Planos desenvolvido por Pablo Henrique Oliveira Rodrigues.") 
# Input do valor base do plano que será usado para o cálculo
valorBase = float(input("Informe o valor base do plano: "))
# Input da idade do cliente que será usado para o cálculo
idade = int(input("Informe a idade do cliente: "))
# Sequência de condicionais que estabelecem o cálculo e armazenam o valor na variável
if idade >= 0 and idade < 19:
    valorMensal = valorBase * 100/100
elif idade >= 19 and idade < 29:
    valorMensal = valorBase * 150/100
elif idade >= 29 and idade < 39:
    valorMensal = valorBase * 225/100
elif idade >= 39 and idade < 49:
    valorMensal = valorBase * 240/100
elif idade >= 49 and idade < 59:
    valorMensal = valorBase * 350/100
else: # Encerramento da sequência, onde se nenhuma das condições anteriores forem atendidas, é realizado o cálculo de idade maior que 59 anos
    valorMensal = valorBase * 600/100
# Exibição do valor final do plano com 2 casas
print(f"O valor mensal do plano é de R$ {valorMensal:.2f}")