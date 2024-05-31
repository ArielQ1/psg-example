comidas = {"carne" : {"animales": ["león", "tigre"]}, "frutas" : {"animales": ["mono", "elefante"]}}

comidas.update(vegetales={"animales": ["elefante", "jirafa"]}, pescado={"animales": ["foca", "pingüino"]},
    insectos={"animales": ["rana", "pájaro carpintero"]}, semillas={"animales": ["loro", "periquito"]})

print(comidas)

print('carne' in comidas)

del comidas['frutas']

print(comidas)