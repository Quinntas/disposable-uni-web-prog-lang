# Título da tabela
print("Tabela de Conversão: Polegadas para Centímetros\n")
print("{: <10} {: <10}".format("Polegadas", "Centímetros"))
print("=" * 25)

# Loop para imprimir a tabela de 1 a 20
for polegadas in range(1, 21):
    centimetros = polegadas * 2.54
    print("{: <10} {: <10.2f}".format(polegadas, centimetros))