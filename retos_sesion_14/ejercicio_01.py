#Un estudiante desea saber cuál es su promedio de calificaciones en la materia de matemáticas, cree una función que reciba las calificaciones como lista y devuelva el promedio las calificaciones son 20,40,60,51,13
calificaciones = [20,40,60,51,13]

def promedio_calificaciones(*args):
    notas = list(args[0])
    return sum(notas) / len(notas)

print(promedio_calificaciones(calificaciones))

