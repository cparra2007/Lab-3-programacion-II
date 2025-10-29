class IteradorMayusculas:
    def __init__(self, lista):
        self.lista = lista
        self.indice = 0 

    def __iter__(self):
        return self 

    def __next__(self): #devuelve el siguiente elemento de la lista en mayusculas
        if self.indice < len(self.lista):
            resultado = self.lista[self.indice].upper()
            self.indice += 1 
            return resultado
        else:
            raise StopIteration

#prueba
print("iterador de mayusculas:")

cadenas = ["hola", "soy", "mesi"]
mi_iterador = IteradorMayusculas(cadenas)

# El bucle llama a iter una vez y depues a next repetidamente
for palabra in mi_iterador:
    print(palabra)

    