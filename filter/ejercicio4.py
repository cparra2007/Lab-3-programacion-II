numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#lambda devuelve true si el resto de la division por 2 no es 0
impares = list(filter(lambda x: x % 2 != 0, numeros))

print("numeros impares")
print(f"lista original: {numeros}")
print(f"filtrados: {impares}")

