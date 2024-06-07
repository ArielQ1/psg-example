#Crear una función que reciba una lista de números y devuelva solo los números pares
def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

# Ejemplo de uso
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = filtrar_pares(lista_numeros)
print(f"Los números pares en la lista son: {numeros_pares}")