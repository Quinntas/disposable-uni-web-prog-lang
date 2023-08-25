# Lê a temperatura em graus Celsius
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Verifica o tipo de clima com base na temperatura
if temperatura_celsius <= 18:
    clima = "frio"
elif 19 <= temperatura_celsius <= 23:
    clima = "agradável"
elif 24 <= temperatura_celsius <= 35:
    clima = "quente"
else:
    clima = "muito quente"

# Exibe a mensagem correspondente ao tipo de clima
print(f"O clima é {clima}.")