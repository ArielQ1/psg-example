#Imprimir un tablero de ajedrez de 8x8 con los caracteres # y *
filas = 8
columnas = 8

for i in range(filas):
    for j in range(columnas):
        if (i + j) % 2 == 0:
            print('#', end=' ')
        else:
            print('*', end=' ')
    print()