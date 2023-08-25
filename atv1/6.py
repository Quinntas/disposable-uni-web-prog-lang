# Lê a velocidade máxima permitida e a velocidade do motorista
velocidade_maxima = int(input("Digite a velocidade máxima permitida (em km/h): "))
velocidade_motorista = int(input("Digite a velocidade do motorista (em km/h): "))

# Calcula a diferença entre a velocidade do motorista e a velocidade máxima
diferenca_velocidade = velocidade_motorista - velocidade_maxima

# Verifica a multa correspondente com base na diferença de velocidade
if diferenca_velocidade <= 10:
    multa = 50
elif 11 <= diferenca_velocidade <= 30:
    multa = 100
else:
    multa = 200

# Mostra a multa que o motorista vai receber
print(f"Multa a ser paga: R$ {multa}")