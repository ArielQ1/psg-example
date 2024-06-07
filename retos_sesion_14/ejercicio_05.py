#Crear una función que reciba una cadena y devuelva la cadena invertida
def invertir_cadena(cadena):
    return cadena[::-1]
cadena = "Hola Mundo"
cadena_invertida = invertir_cadena(cadena)
print(f"La cadena invertida de '{cadena}' es: '{cadena_invertida}'")