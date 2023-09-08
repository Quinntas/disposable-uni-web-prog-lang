input_string = input("Digite uma string: ")
for char in input_string:
    print(char)

# Validação de e-mail
email = input("Digite um endereço de e-mail: ")

# Verifica se contém um caractere "@"
if "@" not in email:
    print("O e-mail deve conter um caractere @.")
elif email[0] == "@":
    print("O @ não pode ser o primeiro caractere.")
elif email[-1] == "@":
    print("O @ não pode ser o último caractere.")
elif len(email) < 10:
    print("O e-mail deve conter pelo menos 10 caracteres.")
elif not email.endswith(".com"):
    print("O e-mail deve terminar com .com.")
else:
    print("O e-mail é válido.")
