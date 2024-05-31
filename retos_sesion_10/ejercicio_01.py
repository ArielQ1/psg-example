Anita =  {"Sushi", "Pizza", "Tacos", "Hamburguesa", "Pasta", "Alitas"}
Pepito = {"Pizza", "Tacos", "Ensalada", "Pasta", "Helado", "Milanesa"}

platos_comunes = Anita.intersection(Pepito)
print("Ambos seguiran saliendo ? : ")
print(len(platos_comunes) >= (int(((len(Anita) + len(Pepito))/2)*.5)))