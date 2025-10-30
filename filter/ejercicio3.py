numeros = [10, 60, 30, 80, 50, 100]

#lambda devuelve true si el numero es mayor que 50
mayores_a_50 = list(filter(lambda x: x > 50, numeros))

print("numeros mayores a 50: ")
print(f"lista original: {numeros}")
print(f"filtrados: {mayores_a_50}")

