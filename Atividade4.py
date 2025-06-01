# Exercício 4- Cadastro de pessoas
# Descrição:
# Crie um programa que:
# Peça o nome e a idade de várias pessoas.
# O cadastro deve continuar enquanto a resposta for S. Ao final, o programa deve exibir:
# Quantas pessoas foram cadastradas.
# A média de idade do grupo.
# O nome da pessoa mais velha cadastrada.

cadastros = []

while True:

    # Nome
    nome = input("Digite o nome da pessoa: ")
    print("=======================================================")
    if nome == "":
        print("Nome inválido. Informe um nome.")
        print("=======================================================")
        continue
    elif nome == "0":
        print("Nome inválido. Informe um nome.")
        print("=======================================================")
        continue
    elif nome.isdigit():
        print("Nome inválido. Informe um nome.")
        print("=======================================================")
        continue
                    
    # Idade
    idade = input("Digite a idade da pessoa: ")
    print("=======================================================")       
    if idade.isalpha():
        print("Idade inválida. Informe um número inteiro.")
        print("=======================================================")
        continue   
    if idade == "":
        print("Você não inseriu nenhum valor, tente novamente.")
        print("=======================================================")
        continue                    
    if idade == "0":
        print("Idade inválida. Informe um número inteiro maior que zero.")
        print("=======================================================")
        continue
    idade = int(idade)

    # Armazenar os dados
    cadastros.append((nome, idade))

    # Continuar cadastro.
    resposta = input("Deseja continuar o cadastro de pessoa? Digite S para continuar ou N para encerrar: ").strip().upper()
    print("=======================================================")
    if resposta == "S":        
        continue
    elif resposta == "N":
        print("Cadastro encerrado.")
        print("=======================================================")
        break
    else:
        print("Resposta inválida. Informe S ou N.")
        continue



# Exibir todos os cadastros
print("\n=== PESSOAS CADASTRADAS ===")
for nome, idade in cadastros:  
    print(f"Nome: {nome} | Idade: {idade} anos")  

# Calcular a média das idades
soma = sum(idade for _, idade in cadastros) 
media = soma / len(cadastros) 
print(f"\nMédia de idade: {media:.2f} anos")  

# Encontrar a pessoa mais velha
maisvelho = max(cadastros, key=lambda x: x[1]) 
print(f"\nPessoa mais velha: {maisvelho[0]} ({maisvelho[1]} anos)") 

# METODO NÃO TÃO EFICIENTE 'continue' melhor apenas repetir outro while dentro do while principal
    
   
