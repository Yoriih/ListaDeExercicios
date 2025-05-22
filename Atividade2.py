# Exercício 2 - Lista de compras

# Peça ao usuário para informar quantos itens deseja adicionar a uma lista de compras.
pedido = int(input("Quantos itens deseja adicionar a lista de compras? "))
# Depois:
listas = []
# Use um for para pedir o nome de cada item.
for i in range(pedido):
    nome = input(f"Digite o nome do item {i + 1}: ")
    listas.append(nome)
    listas.sort()
# Ao final, mostre:
# a) A lista completa de itens.
# b) Quantos itens a lista possui.
# c) A lista em ordem alfabética.
print(f"A lista possui {pedido} itens, sendo eles: {listas} | ")