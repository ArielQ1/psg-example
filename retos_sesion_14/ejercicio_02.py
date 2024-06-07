#Calculadora flexible: Crea una calculadora que acepte diferentes operaciones matemáticas como argumentos de palabras clave y realice los cálculos correspondientes, las operaciones son suma, resta, multiplicación y división
def calculadora_flexible(*args):
    """
    Calculadora flexible que acepta diferentes operaciones matemáticas como argumentos de palabras clave
    y realiza los cálculos correspondientes.\n
    numero1 operador numero2
    """
    if len(args) != 3:
        return "Error: Debe proporcionar 3 argumentos"
    num1, operacion, num2 = args
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicación":
        return num1 * num2
    elif operacion == "división":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: No se puede dividir entre cero"
print(calculadora_flexible(10, "suma", 5))  # Output:
print(calculadora_flexible(10, "resta", 5))  # Output
print(calculadora_flexible(10, "multiplicación", 5))  # Output
print(calculadora_flexible(10, "división", 5))  # Output

