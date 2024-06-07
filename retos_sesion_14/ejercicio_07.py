def crear_tablero():
    return [[' ' for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print('|'.join(fila))
        print('-' * 5)

def realizar_jugada(tablero, jugador, fila, columna):
    fila -= 1
    columna -= 1
    if tablero[fila][columna] == ' ':
        tablero[fila][columna] = jugador
        return True
    else:
        return False

def verificar_ganador(tablero, jugador):
    # Verificar filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True
    
    # Verificar columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True
    
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    
    return False

def tablero_lleno(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == ' ':
                return False
    return True

def jugar_tres_en_raya():
    tablero = crear_tablero()
    jugador_actual = 'X'
    
    while True:
        mostrar_tablero(tablero)
        entrada = input(f"Jugador {jugador_actual}, ingrese su jugada (fila,columna) o 'salir' para terminar: ").strip().lower()
        if entrada == 'salir':
            print("Juego terminado.")
            break

        if ',' in entrada:
            fila, columna = entrada.split(',')
            if fila.isdigit() and columna.isdigit():
                fila = int(fila)
                columna = int(columna)
                if 1 <= fila <= 3 and 1 <= columna <= 3:
                    if realizar_jugada(tablero, jugador_actual, fila, columna):
                        if verificar_ganador(tablero, jugador_actual):
                            mostrar_tablero(tablero)
                            print(f"¡Jugador {jugador_actual} ha ganado!")
                            break
                        elif tablero_lleno(tablero):
                            mostrar_tablero(tablero)
                            print("¡Es un empate!")
                            break
                        jugador_actual = 'O' if jugador_actual == 'X' else 'X'
                    else:
                        print("Movimiento inválido. La celda ya está ocupada.")
                else:
                    print("Los números de fila y columna deben estar entre 1 y 3.")
            else:
                print("Entrada inválida. Por favor, ingrese números válidos para fila y columna.")
        else:
            print("Entrada inválida. Por favor, ingrese fila y columna como dos números separados por una coma.")

jugar_tres_en_raya()
