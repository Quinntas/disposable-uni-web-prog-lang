# Lê os dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Mostra o menu de opções
print("Escolha a opção:")
print("1- Soma de 2 números.")
print("2- Diferença entre 2 números (maior pelo menor).")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")

# Lê a opção do usuário
opcao = int(input("Digite o número da opção desejada: "))

# Executa a operação de acordo com a opção escolhida
if opcao == 1:
    resultado = numero1 + numero2
elif opcao == 2:
    resultado = abs(numero1 - numero2)  # Diferença sempre positiva
elif opcao == 3:
    resultado = numero1 * numero2
elif opcao == 4:
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Erro: Divisão por zero não é permitida.")
        resultado = None
else:
    print("Opção inválida.")
    resultado = None

# Mostra o resultado se a operação for válida
if resultado is not None:
    print("Resultado:", resultado)