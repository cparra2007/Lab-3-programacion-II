def fibonacci_diez():
    a, b = 0, 1 
    for _ in range(10): 
        yield a         
        a, b = b, a + b  # actualiza los valores para la siguiente vuelta

# prueba
print("10 primeros fibonacci:")

for numero in fibonacci_diez():
    print(numero)
