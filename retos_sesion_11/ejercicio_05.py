arca = {"perro" : 2, "gato" : 2, "tigre" : 2, "mono" : 2, "unicornio" : 0, "jirafa" : 1}
print(arca)

arca.update({"leon" : 2, "elefante" : 1})
print(arca)

animales = list(arca.keys())
print(animales)

print("dragon" in arca)

del arca["unicornio"]
print(arca)

arca["jirafa"] = 2
print(arca)

arca.clear()