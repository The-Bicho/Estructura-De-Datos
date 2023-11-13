# Pedir al usuario la longitud del vector
longitud = int(input("Ingrese la longitud del vector: "))

# Crear una lista vacía para el vector
vector = []

# Pedir al usuario que ingrese los elementos del vector
for i in range(longitud):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    vector.append(elemento)

# Imprimir el vector generado
print("El vector generado es:", vector)
