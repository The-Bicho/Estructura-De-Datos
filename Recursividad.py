def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
numero = int(input("Ingresa un número para calcular su factoria: "))

resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
