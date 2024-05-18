#Ejercicio 3
interuptor_1 = True
interuptor_2 = True
print(f"Interruptor 1 esta: {interuptor_1} y el interruptor 2 esta: {interuptor_2}, entonces la puerta se: ",not((interuptor_1 or interuptor_2) and not(interuptor_1 and interuptor_2)))
interuptor_1 = True
interuptor_2 = False
print(f"Interruptor 1 esta: {interuptor_1} y el interruptor 2 esta: {interuptor_2}, entonces la puerta se: ",not((interuptor_1 or interuptor_2) and not(interuptor_1 and interuptor_2)))
interuptor_1 = False
interuptor_2 = True
print(f"Interruptor 1 esta: {interuptor_1} y el interruptor 2 esta: {interuptor_2}, entonces la puerta se: ",not((interuptor_1 or interuptor_2) and not(interuptor_1 and interuptor_2)))
interuptor_1 = False
interuptor_2 = False
print(f"Interruptor 1 esta: {interuptor_1} y el interruptor 2 esta: {interuptor_2}, entonces la puerta se: ",not((interuptor_1 or interuptor_2) and not(interuptor_1 and interuptor_2)))