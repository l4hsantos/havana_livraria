import datetime

livros = []  # (id, título, autor, ano, preço, estoque)
compras = []  # (itens, total, data)

def boas_vindas():
    print("—" * 60)
    print("     BEM-VINDO À LIVRARIA DAS CARTAS PERDIDAS".center(60))
    print("—" * 60)
    print(" Um lugar onde cada livro possui uma história esperando para ser reencontrada.\nA sua próxima grande aventura está a uma página de distância.")
    print()

def cadastrar_livro():
    print("\n Cadastre o livro seguindo os dados abaixo")
    print("Alerta: O 'id' só deve possuir números")
    IDF = input("Digite o 'id'(identificador) do livro: ")
    titulo = input("Digite o título do livro: ").upper()
    autor = input("Digite o nome do autor: ").upper()
    ano = input("Digite o ano que o livro foi públicado: ")
    preco = float(input("Digite o preço do livro: ").replace(",", "."))
    estoque = int(input("Digite quantos livros têm no estoque: "))

    livros.append((IDF, titulo, autor, ano, preco, estoque))
    print(f"\nO cadastro do livro '{titulo}' foi realizado.")

def lista_livro():
    if not livros:
        print("\nNenhum livro foi cadastrado\n")
    else:
        print("\nLivros cadastrados:\n ")
        for livro in livros:
            print(f"ID: {livro[0]}")
            print(f"Título: {livro[1]}")
            print(f"Autor: {livro[2]}")
            print(f"Ano de publicação: {livro[3]}")
            print(f"Preço: R${livro[4]:.2f}")
            print(f"Estoque: {livro[5]} unidades disponíveis")
            print("—" * 40)

def alterar_livro():
    livro_alterar = input("Digite o 'id'(identificador) do livro que você deseja alterar: ")
    for livro in livros:
        IDF, titulo, autor, ano, preco, estoque = livro
        if IDF == livro_alterar:
            novo_titulo = input("Novo título: ").upper()
            novo_autor = input("Novo autor: ").upper()
            novo_ano = input("Novo ano de publicação: ")
            novo_preco = float(input("Novo preço: ").replace(",", "."))
            novo_estoque = int(input("Novo estoque: "))

            confirma = input("Para confirmar digite (1), para cancelar digite (0): ")
            if confirma == "1":
                livros[livros.index(livro)] = (IDF, novo_titulo, novo_autor, novo_ano, novo_preco, novo_estoque)
                print("\nLivro atualizado com sucesso!")
            else:
                print("Alteração cancelada.")
            return
    print("Livro não encontrado.")

def exluir_livro():
    excluir_id = input("Digite o 'id'(identificador) do livro que você deseja excluir: ")
    for i in range(len(livros)):
        if livros[i][0] == excluir_id:
            del livros[i]
            print("O livro foi excluído.")
            return
    print("ID não encontrado.")

# Função do caixa, usando 'achar_livro' como no código original
def registrar_compra():
    print("—" * 60)
    print("REGISTRAR COMPRA - LIVRARIA DAS CARTAS PERDIDAS")
    print("Digite os livros desejados. Quando quiser encerrar, digite 'fim' no ID.\n")

    itens = []
    total = 0.0

    while True:
        id_livro = input("Digite o ID do livro (ou 'fim' para encerrar): ").strip()
        if id_livro.lower() == "fim":
            break

        achar_livro = None
        for livro in livros:
            if livro[0] == id_livro:
                achar_livro = livro
                break

        if achar_livro is None:
            print("Livro não encontrado.")
            continue

        qnt = int(input("Digite a quantidade: "))
        if qnt > achar_livro[5]:
            print("Estoque insuficiente.")
            continue

        subtotal = achar_livro[4] * qnt
        total += subtotal
        itens.append((achar_livro[1], achar_livro[2], qnt, achar_livro[4], subtotal))

        novo_estoque = achar_livro[5] - qnt
        livros[livros.index(achar_livro)] = (*achar_livro[:5], novo_estoque)

    if itens:
        data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        compras.append((itens, total, data))

        print("\n—" * 50)
        print("NOTA FISCAL - LIVRARIA DAS CARTAS PERDIDAS")
        print(f"Data: {data}")
        for item in itens:
            titulo, autor, qnt, preco, subtotal = item
            print(f"{titulo} - {autor} | Quantidade: {qnt} | R${preco:.2f} -> Subtotal: R${subtotal:.2f}")
        print("—" * 50)
        print(f"Total a pagar: R${total:.2f}")
        print("Obrigada pela compra! Volte sempre!\n")
    else:
        print("Nenhum item foi comprado.")

def lista_compra():
    print("\n—" * 60)
    print("REGISTRO DE COMPRAS - LIVRARIA DAS CARTAS PERDIDAS")
    print("—" * 60)

    if not compras:
        print("Nenhuma compra registrada.")
        return

    for compra in compras:
        itens, total, data = compra
        print(f"\nData: {data}")
        for item in itens:
            titulo, autor, qnt, preco, subtotal = item
            print(f"{titulo} - {autor} | Qtd: {qnt} | R${preco:.2f} | Subtotal: R${subtotal:.2f}")
        print(f"Total da compra: R${total:.2f}")
        print("—" * 60)

def menu():
    while True:
        print("—" * 60)
        print(" MENU - LIVRARIA DAS CARTAS PERDIDAS".center(60))
        print("—" * 60)
        print('''
1. Cadastrar um novo livro
2. Lista de livros disponíveis
3. Alterar dados de livro
4. Excluir livro cadastrado
5. Registrar uma nova compra
6. Lista de compras
0. Sair
        ''')

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            lista_livro()
        elif opcao == "3":
            alterar_livro()
        elif opcao == "4":
            exluir_livro()
        elif opcao == "5":
            registrar_compra()
        elif opcao == "6":
            lista_compra()
        elif opcao == "0":
            print("\nEncerrando o sistema...")
            print("Obrigada por visitar a Livraria das Cartas Perdidas!")
            break
        else:
            print("Opção inválida. Tente novamente.")

boas_vindas()
menu()