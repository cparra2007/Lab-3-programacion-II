from functools import reduce

numeros = [2, 3, 4]

producto = reduce(lambda a, b: a * b, numeros)

print("multiplicar elementos:")
print(f"lista original: {numeros}")
print(f"producto total: {producto}")