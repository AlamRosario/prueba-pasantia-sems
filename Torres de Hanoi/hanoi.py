def torre_de_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mueve el disco 1 de {origen} a {destino}")
        return
    # Mueve n-1 discos del origen al auxiliar usando destino como apoyo
    torre_de_hanoi(n-1, origen, destino, auxiliar)
    # Mueve el disco restante directamente al destino
    print(f"Mueve el disco {n} de {origen} a {destino}")
    # Mueve los n-1 discos del auxiliar al destino usando origen como apoyo
    torre_de_hanoi(n-1, auxiliar, origen, destino)

# Pedir al usuario el número de discos
try:
    n = int(input("Ingrese el número de discos: "))

    # Validar que n sea mayor a 0
    if n <= 0:
        print("⚠️ Error: El número de discos debe ser mayor a 0.")
    else:
        torre_de_hanoi(n, 'A', 'B', 'C')

except ValueError:
    print("⚠️ Error: Debe ingresar un número entero válido.")
