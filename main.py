import json 

def carregar_despesas():
    try:
        with open("despesas.json", "r", encoding="utf-8") as ficheiro:
            return json.load(ficheiro)
    except FileNotFoundError:
        return[]

    
despesas = carregar_despesas()

def guardar_despesas():
    with open("despesas.json", "w", encoding="utf-8") as ficheiro:
        json.dump(despesas, ficheiro, ensure_ascii=False, indent=4)



while True:
    print("\n=================================")
    print(" GESTOR DE DESPESAS PESSOAIS")
    print("=================================")
    print("1. Registrar despesa")
    print("2. Ver despesas")
    print("3. Consultar total de gastos")
    print("4. Eliminar despesa")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        while True:
            descricao = input("Descrição da despesa: ").strip()

            if descricao :
                break

            print("A descrição não pode ficar vazia. ")

        while True:
            try:
                valor = float(input("Valor da despesa: "))

                if valor <= 0:
                    print("O valor deve ser maior que zero.")
                    continue

                break

            except ValueError:
                print("Valor inválido. Por favor digite um número válido.")

        despesas.append((descricao, valor))
        guardar_despesas()


        print("Despesa:", descricao)
        print("Valor:", valor,"€")
        print("Despesa guardada!")

    elif opcao == "2":
        print("\n--- AS minhas despesas ---")

        if len(despesas) == 0:
            print("Ainda não existem despesas registradas.")

        else:
            for numero, (descricao, valor) in enumerate(despesas , start=1):
                print(f"{numero}. {descricao} - {valor:.2f} €")


    elif opcao == "3":
        if len(despesas) == 0:
            print("Ainda não existem despesas registradas.")
        else:
            total = 0

            for descricao, valor in despesas:
                total += valor 

            print(f"Total de gastos: {total:.2f} €")

    elif opcao == "4":
        if len(despesas) == 0:
            print("Não existem despesas registradas para eliminar.")

        else:
            print("\n--- Eliminar despesa ---")


            for numero, (descricao, valor) in enumerate(despesas, start=1):
                print(f"{numero}. {descricao} - {valor:.2f} €")
                
            escolha = input("Digite o numero da despesa que deseja eliminar: ")

            try :
                numero = int(escolha)

                if 1 <= numero <= len(despesas):
                    despesa_removida = despesas.pop(numero - 1)
                    guardar_despesas()
                    print(f"Despesa ' {despesa_removida[0]}' eliminada com sucesso.")
                else:
                    print("Numero inválido. Escolha uma despesa da lista.")

            except ValueError:
                print("Entrada inválida. Introduza um numero inteiro.")

            



    elif opcao == "0":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")


