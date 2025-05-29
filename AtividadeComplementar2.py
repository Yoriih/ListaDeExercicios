#Atividade Extra

# Crie um programa que simula um jogo onde um sapo precisa atravessar um rio pulando de pedra em pedra. 
# O sapo começa na pedra 1 e deve chegar até a pedra 4, pulando uma pedra por vez
# (ou seja, de 1 para 2, depois para 3 e finalmente para 4).
# O programa deve:

# Mostrar a pedra onde o sapo está a cada rodada.
# Pedir ao usuário para digitar o número da próxima pedra para onde o sapo deve pular.
# Verificar se a entrada é válida (um único dígito de 1 a 9).
# Verificar se o pulo é correto (apenas para a próxima pedra imediata).
# Informar se o pulo foi correto ou se o sapo caiu na água (em caso de erro ou entrada inválida), encerrando o jogo.
# Caso o sapo chegue até a pedra 4 com sucesso, mostrar uma mensagem de parabéns.
def main():
    pedra_atual = 1
    opcao = 0

    while True:
        print("===================================================")
        print("\n================| JOGO DO SAPINHO |================")
        print("\n===================================================")
        print("1 - JOGAR")
        print("2 - SAIR")
        print("===================================================")
        opcao = int(input("DIGITE SUA OPÇÃO: "))

main()