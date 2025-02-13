def torre_de_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mueve el disco 1 de {origen} a {destino}")
        return
    # Mueve n-1 discos del origen al auxiliar usando destino como apoyo
    torre_de_hanoi(n-1, origen, destino, auxiliar)
    # Mover el disco restante directamente al destino
    print(f"Mueve el disco {n} de {origen} a {destino}")
    # Mover los n-1 discos del auxiliar al destino usando origen como apoyo
    torre_de_hanoi(n-1, auxiliar, origen, destino)

# Pedir al usuario el número de discos
n = int(input("Ingrese el número de discos: "))

# Llamar la función con los palos A (origen), B (auxiliar) y C (destino)
torre_de_hanoi(n, 'A', 'B', 'C')
