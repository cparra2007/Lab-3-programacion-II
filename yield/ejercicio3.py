class Cuadrados:
    def __iter__(self):
        for i in range(1, 11):  
            yield i * i

#pueba clase
print("Cuadrados con clase: ")

# al crear la instancia y usarla en el for
# se llama a __iter__
for numero in Cuadrados():
    print(numero)
    