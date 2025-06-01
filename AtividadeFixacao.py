# Você foi contratado para desenvolver um pequeno sistema de cadastro de cidades para uma pesquisa populacional.
# O programa deve permitir que o usuário cadastre várias cidades, informando:


# A população estimada dessa cidade

cadastros = []
total = 0
while True:

    # NOME DA CIDADE
    cidade = input("INFORME O NOME DA CIDADE: ")
    print("=======================================================")

    if cidade == "":
        print("VOCÊ NÃO INFORMOU UM NOME.")
        print("=======================================================")
        continue
    if cidade == "0":
        print("NÚMEROS NÃO SÃO ACEITOS, APENAS LETRAS.")
        print("=======================================================")
        continue       
    if cidade.isdigit():
        print("NÚMEROS NÃO SÃO ACEITOS, APENAS LETRAS.")
        print("=======================================================")
        continue

    # POPULAÇÃO DA CIDADE
    populacao = input("QUAL A POPULAÇÃO ESTIMADA DA CIDADE? ")
    print("=======================================================")

    if populacao == "":
        print("VOCÊ NÃO INFORMOU A POPULAÇÃO ESTIMADA.")
        print("=======================================================")
        continue
    if populacao.isalpha():
        print("SOMENTE NÚMEROS SÃO ACEITOS.")
        print("=======================================================")
        continue
    if populacao == "0":
        print("ZERO NÃO É UM VALOR VÁLIDO.")
        print("=======================================================")
        continue

    populacao = int(populacao)
    cadastros.append((cidade, populacao))
    total += 1
    

    # PERGUNTA 'FINALIZAR SISTEMA?'
        
    pergunta = input("DESEJA CONTINUAR O CADASTRO? (S/N): ").strip().upper()
    print("=======================================================")
    if pergunta == 'S':
        continue
    elif pergunta == 'N':
        print("ENCERRANDO CADASTROS...")
        print("=======================================================")
        break
    else:
        print("SOMENTE: 'S' PARA SIM | 'N' PARA NÃO .")
        print("=======================================================")
        continue

print("n\ORGANIZANDO CADASTROS FEITOS...")

for cidade, populacao in cadastros:

    # TOTAL DE CIDADES
    print(f"FORAM CADASTRADAS UM TOTAL DE {total} CIDADES")

    # MÉDIA DA POPULAÇÃO DE TODAS CIDADES
    soma = sum(populacao for _, populacao in cadastros) 
    media = soma / len(cadastros) 
    print(f"\nMÉDIA DA POPULAÇÃO: {media:.1f} HABITANTES") 

    # NOME E POPULAÇÃO DA CIDADE MAIS POPULOSA
    maispopulosa = max(cadastros, key=lambda x: x[1]) 
    print(f"\nCIDADE MAIS POPULOSA: {maispopulosa[0]} COM ({maispopulosa[1]} HABITANTES)")
    break

      
# METODO NÃO TÃO EFICIENTE 'continue' melhor apenas repetir outro while dentro do while principal
