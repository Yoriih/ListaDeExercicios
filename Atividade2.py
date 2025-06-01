# Exercício 2 - Lista de compras

# Peça ao usuário para informar quantos itens deseja adicionar a uma lista de compras.
# Depois:
# Use um for para pedir o nome de cada item.
# Ao final, mostre:
# a) A lista completa de itens.
# b) Quantos itens a lista possui.
# c) A lista em ordem alfabética.

listas = []

# Quantidade de itens
while True:  

    pedido = input("Quantos itens deseja adicionar a lista de compras? ")

    if pedido.isalpha():
        print("Caracter inválido. Informe um número maior que 0.")
        print("=======================================================")
        continue       
    if pedido == "0":
        print("Número inválido. Informe um número maior que 0.")
        print("=======================================================")
        continue 
    if pedido == "":
        print("Você não inseriu nenhum valor, tente novamente.")
        print("=======================================================")
        continue                     

    
    break
pedido = int(pedido)

# Laço para coletar os nomes de cada item
for i in range(pedido):   
# Nome
    nome = input(f"Digite o nome do item {i + 1}: ")
    print("=======================================================")
    if nome == "":
        print("Nenhum nome inserido. Informe um nome.")
        continue
    if nome == "0":
        print("0 não é um nome válido. Informe um nome.")
        continue
    if nome.isdigit():
        print("Números não são válidos. Informe um nome.")
        continue

# Quantidade
    quantidade = input(f"Digite a quantidade do item {i+1} - {nome} : ")
    print("=======================================================")     
    if quantidade == "0":
        print("Número inválido. Informe um número maior que 0.")
        continue 
    if quantidade == "":
        print("Você não inseriu nenhum valor, tente novamente.")
        continue
    if quantidade < "0":
        print("Número inválido. Informe um número maior que 0.")
        continue

# Salvar os nomes e quantidades no vetor 'Listas' e Organizar em ordem alfabética.
    listas.append((nome, quantidade))
    
                                 
# Exibir a lista completa
print("\nLista de compras:")
listas.sort()  # Organiza a lista em ordem alfabética

for nome, quantidade in listas:    
    print(f"{nome} - Quantidade: {quantidade}")

print("\nPossuindo um total de", len(listas), "itens.")

# METODO NÃO TÃO EFICIENTE 'continue' melhor apenas repetir outro while dentro do while principal
