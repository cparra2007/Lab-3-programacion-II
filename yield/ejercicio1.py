def primeros_pares():
    for i in range(10):  
        yield i * 2      #yield para entregar el valor

#prueba
print("primeros 10 pares:")
for numero in primeros_pares():
    print(numero)