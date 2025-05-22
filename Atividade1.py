#Exercício 1 - Números primos entre 1 e 100
# Dica: Um número é primo se for divisível apenas por 1 e por ele mesmo.
contador_primos = 0
# Utilize o laço for para verificar e exibir todos os números primos de 1 a 100.
for numero in range(1, 101):
    
    divisores = 0 # Zera a contagem para cada numero
    divisor = 1 # Reinicia o divisor
    
    while divisor <= numero:
        if numero % divisor == 0:
            divisores += 1
        divisor += 1
    
    if divisores == 2:
        print(f"{numero} é primo.")
        contador_primos += 1 # Conta quanto primos foram achados
        
# Ao final, mostre quantos números primos foram encontrados.
print(f"Foram encontrados {contador_primos} de números primos")

   
    