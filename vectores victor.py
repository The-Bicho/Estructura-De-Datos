# Solicitar al usuario la longitud del vector
n = int(input("¿Cual es la longitud del vector?: "))

# Inicializar una lista vacía para el vector
vector = []

# Solicitar al usuario ingresar los elementos del vector uno por uno
for i in range(n):
    elemento = float(input(f"Debes ingresar el elemento {i + 1}: "))
    vector.append(elemento)

# Imprimir el vector generado
print("Vector:", vector)
