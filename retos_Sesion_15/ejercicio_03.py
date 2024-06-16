#Simular un cajero automático que solicite un monto a retirar, si el monto es mayor al saldo lanzar una excepción personalizada y si el monto es mayor a 1000 lanzar una excepción genérica
class SaldoInsuficienteException(Exception):
    pass

saldo = 5000 
while True:
    try:
        monto_retirar = input("Ingrese el monto a retirar (o 'salir' para terminar): ")

        if monto_retirar.lower() == "salir":
            print("¡Gracias por usar el cajero automático!")
            break

        monto = float(monto_retirar)

        if monto > saldo:
            raise SaldoInsuficienteException("Error: Saldo insuficiente para realizar esta operación.")
            
        if monto > 1000:
            raise Exception("Error: No se pueden retirar montos mayores a 1000 en una sola transacción.")
            
        saldo -= monto
        print(f"Retiro exitoso. Su nuevo saldo es: {saldo:.2f} Bs")

    except SaldoInsuficienteException as e:
        print(e)
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese un número.")
    except Exception as e:
        print(e)
