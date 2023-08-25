# Inicializa as variáveis para armazenar o maior e o menor valores
maior_valor = float('-inf')  # Inicializado com o menor valor possível
menor_valor = float('inf')  # Inicializado com o maior valor possível

# Lê os 20 números inteiros
for i in range(20):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))

    # Verifica se o número é maior que o maior_valor atual
    if numero > maior_valor:
        maior_valor = numero

    # Verifica se o número é menor que o menor_valor atual
    if numero < menor_valor:
        menor_valor = numero

# Mostra o maior e o menor valor fornecidos
print(f"O maior valor é: {maior_valor}")
print(f"O menor valor é: {menor_valor}")