palabras = ["uno", "dos", "tres"]

#uso len directo, sin lambda
longitudes = list(map(len, palabras))

print("longitud de palabras: ")
print(f"palabras: {palabras}")
print(f"longitudes: {longitudes}")
