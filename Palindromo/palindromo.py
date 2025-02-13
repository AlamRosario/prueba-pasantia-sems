import re

def es_palindromo(cadena):
    # Convertir la cadena a minúsculas y eliminar espacios y caracteres no alfabéticos
    cadena_limpia = re.sub(r'[^a-zA-Z0-9]', '', cadena.lower())
    
    # Comparar la cadena con su versión invertida
    return cadena_limpia == cadena_limpia[::-1]

# Pedir al usuario una cadena de texto
texto = input("Ingrese una frase o palabra: ")

# Evaluar si es un palíndromo
if es_palindromo(texto):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")