#Crear una serie de números del 1 al 100, si el número es divisible por 3 imprimir Fizz, si el número es divisible por 5 imprimir Buzz, si el número es divisible por 3 y 5 imprimir FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} => FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} => Fizz")
    elif i % 5 == 0:
        print(f"{i} => Buzz")
    else:
        print(i)