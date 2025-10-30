palabras = ["perro", "gato", "pato", "hamster"]

#lambda comprueba si el primer caracter (indice 0) es p
con_p = list(filter(lambda palabra: palabra[0] == "p", palabras))

print("palabras que empiezan con p:")
print(f"lista original: {palabras}")
print(f"filtradas con p: {con_p}")

