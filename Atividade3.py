# Exercício 3 - Caixa eletrônico
# Descrição:
# Simule o funcionamento de um caixa eletrônico que:

notas = [100, 50, 20, 10, 5, 2]

saldo = int(input("Informe o saldo disponível: "))

while True:
     
    valor = input("\nInforme o valor que deseja sacar ou  digite 'sair' para encerrar o programa: ")

    if valor.lower() == 'sair':
            print("Encerrando o programa.")
            break
    if not valor.isdigit():
            print("Valor inválido. Informe um número inteiro.")
            continue
    if valor == "":
            print("Valor inválido. Você não informou um valor.")
            continue
    if valor == "0":
            print("Valor inválido. Informe um número maior que zero.")
            continue
    
    valor = int(valor)

    if valor > saldo:
                print("=======================================================")
                print(f"Valor maior que o saldo disponível. Saldo Disponivel de R$ {saldo}")
                print("=======================================================")
                continue
    if valor < 2: 
                print("=======================================================")
                print("Valor mínimo de R$ 2,00")
                print("=======================================================")
                continue
    
    print(f"\nValor a ser sacado: {valor} reais")
    print("=======================================================")

    for nota in notas:

        quantidade = valor // nota
        if quantidade > 0:
            print(f"Notas para o saque: {quantidade} notas de R${nota},00")
            valor = valor % nota
            saldo -= quantidade * nota        
            break

    print("\nRetire seu dinheiro.")
    print(f"Novo Saldo Disponível: R${saldo},00")
    print("Obrigado por utilizar o nosso caixa eletrônico. Volte Sempre!")
    print("=======================================================")

# METODO NÃO TÃO EFICIENTE 'continue' melhor apenas repetir outro while dentro do while principal

