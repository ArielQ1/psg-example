#Crear una función recursiva para obtener el N número de la serie de Fibonacci
def fibonacci_recursivo(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci_recursivo(numero-1) + fibonacci_recursivo(numero-2)
numero = 6
print(f"El {numero}-ésimo número de Fibonacci es: {fibonacci_recursivo(numero)}")