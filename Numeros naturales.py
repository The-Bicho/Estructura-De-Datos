# Problema Interativo
def suma_iterativa(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma
n = 5
resultado = suma_iterativa(n)
print(resultado)

# Problema Recursivo
def suma_recursiva(n):
    # Condición de salida
    if n == 0:
        return 0
    # Segmento recursivo
    else:
        return n + suma_recursiva(n - 1)

n = 5 
resultado = suma_recursiva(n)
print(f"La suma de los primeros {n} números naturales es: {resultado}")
