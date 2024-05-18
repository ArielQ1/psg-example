print("Construir el operador XNOR en Python")
a = True
b = True
print(f"{a} XNOR {b} ->",not((a or b) and not(a and b)))
a = True
b = False
print(f"{a} XNOR {b} ->",not((a or b) and not(a and b)))
a = False
b = True
print(f"{a} XNOR {b} ->",not((a or b) and not(a and b)))
a = False
b = False
print(f"{a} XNOR {b} ->",not((a or b) and not(a and b)))