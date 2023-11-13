# Pedir al usuario la cantidad de nombres que desea ingresar
num_elementos = int(input("Ingrese la cantidad de nombres que desea ingresar: "))

# Crear una lista vacía para almacenar los números
nombres = []

# Pedir al usuario que ingrese los números y agregarlos a la lista
for i in range(num_elementos):
    nombre = str(input(f"Ingrese el nombre {i + 1}: "))
    nombres.append(nombre)

# Imprimir la lista de nombres ingresados por el usuario
print("Los nombres ingresados son:")
for nombre in nombres:
    print(nombre)
