print ("Inicio Ejemplo 1")
x = 1 / 0
print (x)
print ("Fin Ejemplo 1")

print ("Inicio Ejemplo 1")
try:
    x = 1 / 0
    print (x)
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 1")

#Ejercicio 1
#Crear un programa que solicite dos números y realice la división de ambos números Si hay un error mostrar un mensaje de error El programa se detiene si se ingresa "salir"
while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1 == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2 == "salir":
            break
        num1 = float(num1)
        num2 = float(num2)
        print("Resultado:", num1 / num2)
    except Exception as e:
        print("💀 Error:", e)

#Ejemplo 2, División por cero
print ("Inicio Ejemplo 2")
divisor = 0
try:
    x = 1 / divisor
    print (x)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 2")

#Ejemplo 3
#De la lista de calificaciones obtener el promedio
calificaciones = [20,40,80,"A"]
suma = 0
try:
    for i in range(len(calificaciones)+1):
        suma += calificaciones[i] 
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except TypeError as e:
    print("🎭 Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))

#Ejemplo 4
#De la lista de calificaciones obtener el promedio
print ("Inicio Ejemplo 4")
calificaciones = [20,40,80]
suma = 0
try:
    for i in range(len(calificaciones)):
        suma += calificaciones[i]
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except Exception as e:
    print("💀 Error:", e, type(e))
else:
    print ("🎉 Sin errores")
print ("Fin Ejemplo 4")

#Ejercicio 2
def division(num1, num2):
    return num1 / num2
while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1 == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2 == "salir":
            break
        num1 = float(num1)
        num2 = float(num2)
        resultado = division(num1, num2)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Resultado: ",resultado)

#Ejemplo 5
#Simula una conexión a internet que haga ping y cerrar la conexión
print ("Inicio Ejemplo 5")
try:
    print("🔗 Ping...")
except Exception as e:
    print("💀 Error:", e)
else:
    print("🎉 Ping Exitoso")
finally:
    print("🔌 Cerrando conexión")

#Ejemplo 6
#Simula una conexión a internet que haga ping y cerrar la conexión
print ("Inicio Ejemplo 6")
try:
    print("🔗 Ping...")
    raise Exception("Error de conexión") #Excepción genérica
except Exception as e: # Captura cualquier excepción
    print("💀 Error:", e)
else:
    print("🎉 Ping Exitoso")
finally:
    print("🔌 Cerrando conexión")

#Ejercicio 3
numeros = []
while True:
    try:
        num = input("Ingrese un número: ")
        if num == "salir":
            break
        num = float(num)
        if num == 0:
            raise Exception("No se puede agregar el número 0")
        numeros.append(num)
    except KeyboardInterrupt as e:
        print('🚫 Para salir escriba "salir"')
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Número agregado")
    finally:
        print("Suma:", sum(numeros))

#Ejemplo 7
# Crea una función que no hace nada
print("Inicio Ejemplo 7")
def funcion():
    pass
funcion()
print("Fin Ejemplo 7")

#Ejemplo 8
# Tienes un frutero, saca las frutas mientras no sea un gusano y genera una excepción
print("Inicio Ejemplo 8")
class GusanoError(Exception):
    pass
frutero = ['🍎', '🍌', '🍐', '🐛', '🍇']
for fruta in frutero:
    try:
        if fruta == '🐛':
            raise GusanoError("😱 Ewww!")
        print(fruta)
    except GusanoError as e:
        print("🐛 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
print("Fin Ejemplo 8")

#Ejercicio 4
class NoAlfabeticoError(Exception):
    pass
palabras = []
while True:
    try:
        palabra = input("Ingrese una palabra: ")
        if palabra == "salir":
            break
        if not palabra.isalpha():
            raise NoAlfabeticoError("Solo se permiten letras")
        palabras.append(palabra)
    except NoAlfabeticoError as e:
        print("🚫 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Palabra agregada")
    finally:
        print("Lista:", palabras)

