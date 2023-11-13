# Problema Interativo
def factorial_iterativo(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
n = 5
resultado = factorial_iterativo(n)
print(resultado)

# Problema Reculsivo
def factorial_recursivo(n):
    # Condición de salida
    if n == 0:
        return 1
    # Segmento recursivo
    else:
        return n * factorial_recursivo(n - 1)
n = 5
resultado = factorial_recursivo(n)
print(f"El factorial del numero {n} es: {resultado}")