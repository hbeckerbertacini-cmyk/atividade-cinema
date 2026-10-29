def cadastrar_avaliacao():

    # Recebe e valida a idade
    while True:
        try:
            idade = int(input("Digite a idade do cliente: "))

            if idade <= 0:
                print("Erro: digite uma idade válida.")
            else:
                break

        except ValueError:
            print("Erro: digite apenas números para a idade.")

    # Escolha da avaliação
    print("\nAvaliações disponíveis:")
    print("1. Ótimo")
    print("2. Bom")
    print("3. Regular")
    print("4. Péssimo")

    escolha = input("Escolha a avaliação: ")

    if escolha == "1":
        avaliacao = "Ótimo"

    elif escolha == "2":
        avaliacao = "Bom"

    elif escolha == "3":
        avaliacao = "Regular"

    elif escolha == "4":
        avaliacao = "Péssimo"

    else:
        print("Avaliação inválida.")
        return

    # Salva sem apagar os registros anteriores
    with open("avaliacoes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{idade};{avaliacao}\n")

    print("\nAvaliação cadastrada com sucesso!")


def listar_avaliacoes():

    # Tenta abrir o arquivo
    try:
        with open("avaliacoes.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

    except FileNotFoundError:
        print("\nNenhuma avaliação cadastrada ainda.")
        return

    # Verifica se o arquivo está vazio
    if len(linhas) == 0:
        print("\nNenhuma avaliação cadastrada ainda.")
        return

    print("\n===== AVALIAÇÕES CADASTRADAS =====")

    cliente = 1

    for linha in linhas:

        idade, avaliacao = linha.strip().split(";")

        print(
            f"Cliente {cliente} - Idade: {idade} - Avaliação: {avaliacao}"
        )

        cliente += 1


def consultar_estatisticas():

    # Tenta abrir o arquivo
    try:
        with open("avaliacoes.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

    except FileNotFoundError:
        print("\nNenhuma avaliação cadastrada ainda.")
        return

    # Verifica se não existem avaliações
    if len(linhas) == 0:
        print("\nNenhuma avaliação cadastrada ainda.")
        return

    # Contadores
    total = 0

    otimo = 0
    bom = 0
    regular = 0
    pessimo = 0

    # Dados do mais velho e mais novo
    maior_idade = None
    menor_idade = None

    avaliacao_mais_velho = ""
    avaliacao_mais_novo = ""

    # Percorre todas as avaliações
    for linha in linhas:

        idade, avaliacao = linha.strip().split(";")

        idade = int(idade)

        total += 1

        # Conta cada tipo de avaliação
        if avaliacao == "Ótimo":
            otimo += 1

        elif avaliacao == "Bom":
            bom += 1

        elif avaliacao == "Regular":
            regular += 1

        elif avaliacao == "Péssimo":
            pessimo += 1

        # Verifica o cliente mais velho
        if maior_idade is None or idade > maior_idade:
            maior_idade = idade
            avaliacao_mais_velho = avaliacao

        # Verifica o cliente mais novo
        if menor_idade is None or idade < menor_idade:
            menor_idade = idade
            avaliacao_mais_novo = avaliacao

    # Exibe os resultados
    print("\n===== ESTATÍSTICAS DAS AVALIAÇÕES =====")

    print("Total de respondentes:", total)

    print("Ótimo:", otimo)
    print("Bom:", bom)
    print("Regular:", regular)
    print("Péssimo:", pessimo)

    print("\nRespondente mais velho:")
    print("Idade:", maior_idade, "anos")
    print("Avaliação:", avaliacao_mais_velho)

    print("\nRespondente mais novo:")
    print("Idade:", menor_idade, "anos")
    print("Avaliação:", avaliacao_mais_novo)


# MENU PRINCIPAL
while True:

    print("\n===== SISTEMA DE AVALIAÇÃO DO CINEMA =====")
    print("1. Cadastrar avaliação")
    print("2. Listar avaliações")
    print("3. Consultar estatísticas")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_avaliacao()

    elif opcao == "2":
        listar_avaliacoes()

    elif opcao == "3":
        consultar_estatisticas()

    elif opcao == "4":
        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpção inválida. Escolha uma opção de 1 a 4.")