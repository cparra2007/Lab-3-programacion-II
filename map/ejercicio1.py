numeros = [1, 2, 3, 4, 5]

#funcion lambda que multiplica x 10
multiplicar = lambda x: x * 10

#map para aplicar lambda a cada elemento
#map devuelve un objeto map que lo convertimos a lista
multiplicados = list(map(multiplicar, numeros))

print("multiplicar por 10: ")
print(f"original: {numeros}")
print(f"multiplicados: {multiplicados}")