#Crear una calculadora que solicite dos números y realice las operaciones básicas de suma, resta, multiplicación y división con manejo de excepciones, para salir del programa se debe ingresar "salir"
while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1.lower() == "salir":
            print("¡Gracias por usar la calculadora!")
            break
        num2 = input("Ingrese el segundo número: ")
        if num2.lower() == "salir":
            print("¡Gracias por usar la calculadora!")
            break
        num1 = float(num1)
        num2 = float(num2)
    except KeyboardInterrupt as e:
        print('🚫 Para salir escriba "salir"')
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese números.")
        continue

    try:
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        print(f"División: {num1} / {num2} = {division}")
    except ZeroDivisionError:
        print("Error💀: No se puede dividir por cero.")

    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print(f"Suma: {num1} + {num2} = {suma}")
        print(f"Resta: {num1} - {num2} = {resta}")
        print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
        