class Impares:
    def __iter__(self):
        for i in range(1, 21): 
            if i % 2 != 0:    
                yield i

#prueba
print("impares 1 al 20 con clase y for")

#for llama a iter
for numero in Impares():
    print(numero)
