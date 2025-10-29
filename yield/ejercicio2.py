def filtrar_impares(numeros):
    for numero in numeros:
        if numero % 2 != 0:  
            yield numero     #devuelve el numero impar y se pausa

#prueba
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("filtrar impares: ")
for impar in filtrar_impares(mi_lista):
    print(impar)

    