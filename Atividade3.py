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
            print("Valor inválido. Informe um número inteiro.")
            continue
    if valor == "0":
            print("Valor inválido. Informe um número inteiro.")
            continue
    
    valor = int(valor)

    if valor > saldo:
            print("=======================================================")
            print("Valor maior que o saldo disponível.")
            print("=======================================================")
            continue
    
    print(f"\nValor a ser sacado: {valor} reais")
    print("=======================================================")

    for nota in notas:

        quantidade = valor // nota
        if quantidade > 0:
            print(f"Notas para o saque: {quantidade} de R${nota},00")
            valor = valor % nota
            saldo -= quantidade * nota
        
            break

    print(f"Novo Saldo Disponível: R${saldo},00")
    print("=======================================================")


