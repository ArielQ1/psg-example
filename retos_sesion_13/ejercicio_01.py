#Imprimir los 20 primeros números de la serie de Fibonacci
primero = contador = 0
segundo = 1
# 0, 1, 1, 2, 3, 5, 8, 12
while contador < 20:
    contador += 1
    luego = primero + segundo
    print(luego, end=", ")
    primero = segundo
    segundo = luego