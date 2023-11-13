def suma_digitos(numero):
    # Condición de salida: Si el número es un solo dígito, devolvemos ese dígito.
    if numero < 10:
        return numero
    # Segmento recursivo: Sumamos el último dígito y llamamos recursivamente para el resto del número.
    else:
        ultimo_digito = numero % 10
        resto_numero = numero // 10
        return ultimo_digito + suma_digitos(resto_numero)

# Solicitar al usuario un número entero
numero = int(input("Ingresa un número entero: "))

# Calcular la suma de sus dígitos utilizando la función recursiva
resultado = suma_digitos(numero)

# Imprimir el resultado
print(f"La suma de los dígitos de {numero} es: {resultado}")
