# Cadastro de Produtos e Estoque
# Você irá criar um programa simples para ajudar a controlar o estoque de uma loja.
# O programa deve permitir que o usuário cadastre vários produtos, informando:

produtos = []
total = 0

print("===============| CADASTRO DE PRODUTOS E QUANTIDADE |===============")
while True:
    
    # NOME DO PRODUTO
    while True:
        nome = input("\nDIGITE O NOME DO PRODUTO: ").strip().title()
        print("=======================================================")

        if not nome.isalpha():
            print("NENHUM NOME DIGITADO OU CARACTER INVÁLIDO. TENTE NOVAMENTE")
            print("=======================================================")
      
        else:
           break # nome será válidado e sair do while
       
       

    # QUANTIDADE DO PRODUTO NO ESTOQUE
    while True:
        estoque = input("QUAL A QUANTIDADE DISPONIVEL NO ESTOQUE? ")
        print("=======================================================")
        
        if not estoque.isdigit():
            print("QUANTIDADE INVÁLIDA. TENTE NOVAMENTE!")
            print("=======================================================")
        else:
            estoque = int(estoque)
            break

    # SOMANDO PARA O TOTAL FINAL E ARMAZENANDO DADOS NO VETOR    
    total += 1
    produtos.append((nome, estoque))

    # PERGUNTAR SE DESEJA CONTINUAR O CADASTRO
    # PERGUNTAR SE DESEJA CONTINUAR O CADASTRO
    while True:
        pergunta = input("VOCÊ DESEJA CONTINUAR O CADASTRO DOS PRODUTOS? (S/N)").strip().upper()
        print("=======================================================")

        if pergunta == "NÃO":
            break       
        elif pergunta == "NAO":            
            break    
        elif pergunta == "S":
            break
        elif pergunta == "SIM":
            break
        elif pergunta.isdigit():
            print("INFORME SIM OU NÃO!")
            print("=========================================")
        elif pergunta == "":
            print("INFORME SIM OU NÃO!")
            print("=========================================")
        elif not pergunta.isalpha():
            print("INFORME SIM OU NÃO!")
            print("=========================================")
            
    # Quando sair do loop, encerra tudo.    
    if pergunta == "NÃO":
        print("ENCERRANDO SISTEMA DE CADASTRO...")
        print("=========================================")
        break       
    elif pergunta == "NAO":
        print("ENCERRANDO SISTEMA DE CADASTRO...")
        print("=========================================")
        break          
        


print("\n=========|ORGANIZANDO INFORMAÇÕES CADASTRADAS|=========")
   
   # TOTAL
print(f"\nFORAM CADASTRADOS UM TOTAL DE {total} ITENS.")

   # SOMA / MÉDIA
soma = sum(estoque for _,estoque in produtos)
media = soma / len(produtos)
print(f"A SOMA TOTAL DAS QUANTIDADES DOS ITENS E DE: {soma} und.")
print(f"A MÉDIA TOTAL É DE: {media:.2f}")

   # MAIOR QUANTIDADE
maior_quantidade = max(produtos,key= lambda x: x[1])
print(f"O ITEM COM MAIOR QUANTIDADE DE É: {maior_quantidade[0]} COM {maior_quantidade[1]} und.")
print("=======================================================")
