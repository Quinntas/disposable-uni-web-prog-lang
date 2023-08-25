# Solicita ao usuário para inserir um número inteiro positivo N
N = int(input("Digite um número inteiro positivo N: "))

# Inicializa a variável para armazenar a soma
soma = 0

# Faz a soma de todos os números inteiros de 1 a N
for i in range(1, N + 1):
    soma += i

# Mostra o resultado da soma
print(f"A soma dos números de 1 a {N} é: {soma}")