# Mensagem de boas-vindas do sistema
print("Bem-vindo a Lista de Contatos de Pablo Henrique Oliveira Rodrigues")

# Cria a lista e define o ID/RU inicial
lista_contatos = []
id_global = 4947927

# Função que cadastra o novo contato quando chamada
def cadastrar_contato(id):
    print("---------------- MENU CADASTRAR CONTATO ----------------")
    print(f"Id do Contato: {id}")
    nome = input("Por favor entre com o nome do Contato: ")
    atividade = input("Por favor entre com a Atividade do contato: ")
    telefone = input("Por favor entre com o telefone do contato: ")

    # Armazena as informações cadastradas nos inputs
    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }
    # Adiciona uma cópia para a lista de contatos
    lista_contatos.append(contato.copy())

# Função que consulta os contatos cadastrados quando chamada
def consultar_contatos():
    while True:
        print("---------------- MENU CONSULTAR CONTATOS ----------------")
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Contatos")
        print("2 - Consultar Contato por id")
        print("3 - Consultar Contato(s) por Atividade")
        print("4 - Retornar")
        opcao = input(">> ")
        # Inicia as condicionais conforme o valor inserido no input anterior
        # Opção 1 Consulta e apresenta todos os contatos cadastrados
        if opcao == "1":
            print("----------------------------------------")
            for contato in lista_contatos:
                print(f"id: {contato['id']}")
                print(f"nome: {contato['nome']}")
                print(f"atividade: {contato['atividade']}")
                print(f"telefone: {contato['telefone']}")
                print()
            print("----------------------------------------")
        # Opção 2 Pergunta o id do contato, o consulta e apresenta   
        elif opcao == "2":
            id_consulta = int(input("Digite o id do contato: "))
            print("----------------------------------------")
            encontrado = False
            for contato in lista_contatos:
                if contato["id"] == id_consulta:
                    print(f"id: {contato['id']}")
                    print(f"nome: {contato['nome']}")
                    print(f"atividade: {contato['atividade']}")
                    print(f"telefone: {contato['telefone']}")
                    print()
                    encontrado = True
                    break
            if not encontrado:
                print("Id inválido")
            print("----------------------------------------")
        # Opção 3 Pergunta a atividade do contato, o consulta e apresenta todos os contatos com aquela atividade   
        elif opcao == "3":
            atividade_consulta = input("Digite a Atividade do(s) Contato(s): ")
            print("----------------------------------------")
            encontrado = False
            for contato in lista_contatos:
                if contato["atividade"].lower() == atividade_consulta.lower():
                    print(f"id: {contato['id']}")
                    print(f"nome: {contato['nome']}")
                    print(f"atividade: {contato['atividade']}")
                    print(f"telefone: {contato['telefone']}")
                    print()
                    encontrado = True
            if not encontrado:
                print("Nenhum contato encontrado com essa atividade.")
            print("----------------------------------------")
        # Opção 4 Retorna ao menu    
        elif opcao == "4":
            return
            
        else:
            print("Opção inválida")
# Função que remove um contato quando chamada
def remover_contato():
    while True:
        print("------------------ MENU REMOVER CONTATO ------------------")
        try:
            # Busca e remove da lista o contato conforme o ID proporcionado
            id_remover = int(input("Digite o id do contato a ser removido: "))
            removido = False
            for contato in lista_contatos:
                if contato["id"] == id_remover:
                    lista_contatos.remove(contato)
                    print("Contato removido com sucesso!")
                    removido = True
                    return
            if not removido:
                print("Id inválido")
        except ValueError:
            print("Id inválido")
# Menu principal responsável por chamar as funções anteriores conforme input do usuário
while True:
    print("-------------------- MENU PRINCIPAL --------------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Contato")
    print("2 - Consultar Contato(s)")
    print("3 - Remover Contato")
    print("4 - Sair")
    opcao_principal = input(">> ")
    # Inicia as condicionais que chama cada função a depender do escolhido pelo usuário
    if opcao_principal == "1":
        cadastrar_contato(id_global)
        id_global += 1
    elif opcao_principal == "2":
        consultar_contatos()
    elif opcao_principal == "3":
        remover_contato()
    elif opcao_principal == "4":
        break
    else:
        print("Opção inválida")