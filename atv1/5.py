# Solicita ao usuário para inserir um número
numero = int(input("Digite um número: "))

# Verifica se o número é múltiplo de 5
if numero % 5 == 0:
    print(f"O número {numero} é múltiplo de 5.")
else:
    print(f"O número {numero} não é múltiplo de 5.")