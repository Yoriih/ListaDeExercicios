# Caixa de Doação de Alimentos
# Você foi contratado para desenvolver um sistema simples de um Calxa de Doação de Alimentos.
# Esse sistema deve ajudar a organizar doações de alimentos, distribuindo os quilos doados em pacotes padronizados de 5kg, 2kg e 1kg, de forma que o número total de pacotes usados seja o menor possivel.
# Requisitos:
# O sistema deve perguntar ao usuário quantos quilos ele deseja doar.
# A doação só será aceita se for de 1 kg ou mais.
# O sistema não deve aceitar entradas inválidas (como letras, simbolos ou números negativos).
# Após receber um valor válido, o programa deve:
# Exibir como a doação será embalada usando os pacotes de 5kg, 2kg e 1kg:
# Mostrar quantos pacotes de cada tipo serão usados;
# Exibir uma mensagem de agradecimento ao final.



print("\n================| CAIXA DE DOAÇÃO |================")


while True:

    doacao = input("\nQUANTOS QUILOS VOCÊ DESEJA DOAR? ")
    print("=======================================================")  

    
    if doacao.isalpha():
        print("Você não pode utilizar letras, apenas números.")
        print("=======================================================")
        continue
    if doacao == "":
        print("Você não pode deixar o campo em branco.")
        print("=======================================================")
        continue
    if doacao[0] == "-":
        print("Você não pode doar menos de 1 quilograma.")
        print("=======================================================")
        continue
    if doacao == '0':
        print("Você não pode doar menos de 1 quilograma.")
        print("=======================================================")
        continue

    doacao = int(doacao)
    
    break

pacotes = [5, 2, 1]

# Exibir como a doação será embalada usando os pacotes de 5kg, 2kg e 1k:

for pacote in pacotes:
    quantidade_pacote = doacao // pacote
    doacao = doacao % pacote
    if quantidade_pacote > 0:
        print("\n================| DOAÇÃO EMBALADA |================")
        print(f"\nSerão usados {quantidade_pacote} x pacotes de {pacote}kg")
        print("\nOBRIGADO POR SUA DOAÇÃO!")


# METODO NÃO TÃO EFICIENTE 'continue' melhor apenas repetir outro while dentro do while principal

        


