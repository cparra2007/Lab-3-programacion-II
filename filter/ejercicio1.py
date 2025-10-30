numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#lambda tiene devolver true para incluir o false para excluir
#x % 2 == 0 devuelve True si x es par
pares = list(filter(lambda x: x % 2 == 0, numeros))

print("numeros pares: ")
print(f"lista original: {numeros}")
print(f"lista filtrada: {pares}")
