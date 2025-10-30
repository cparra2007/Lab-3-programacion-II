from functools import reduce

palabras = ["hola", "mundo", "!"]

frase = reduce(lambda a, b: a + b, palabras)

print("concatenar cadenas: ")
print(f"lista original: {palabras}")
print(f"frase: {frase}")
