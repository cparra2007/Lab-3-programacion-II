numeros = [1, 2, 3, 4, 5]

#lambda eleva al cuadrado 
cuadrados = list(map(lambda x: x * x, numeros))

print("cuadrados de numeros:")
print(f"numeros originales: {numeros}")
print(f"numeros al cuadrado: {cuadrados}")

