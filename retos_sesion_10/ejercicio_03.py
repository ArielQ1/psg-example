#  Ejercicio 3
mochilero_a = {"París", "Londres", "Nueva York", "Tokio", "Peru", "Chile", "Colombia", "Bolivia"}
mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney", "Argentina","Brasil","Panama","Bolivia"}

lugar_no_visitado_a = mochilero_b - mochilero_a
lugar_no_visitado_b = mochilero_a - mochilero_b

print("Lugares que ha visitado mochilero B y no mochilero A: ", lugar_no_visitado_a)
print("Lugares que ha visitado mochilero A y no mochilero B: ", lugar_no_visitado_b)

#  Ejercicio 4 
print("Lugares visitados por ambos mochileros: ", mochilero_a.intersection(mochilero_b))