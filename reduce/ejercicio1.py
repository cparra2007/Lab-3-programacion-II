from functools import reduce

numeros = [5, 10, 15, 20]

suma = reduce(lambda a, b: a + b, numeros)

print("sumar elementos:")
print(f"lista original: {numeros}")
print(f"suma total: {suma}")
