def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Mostra os números de Fibonacci até o 20º termo
for i in range(21):
    fib_number = fibonacci(i)
    print(f"Fibonacci({i}) = {fib_number}")