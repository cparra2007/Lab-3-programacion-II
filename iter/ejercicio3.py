class CuadradosLista:
    def __init__(self, n=10):
        self.n = n

    def obtener_lista(self):
        resultado = []
        for i in range(1, self.n + 1):
            resultado.append(i * i) 
        
        return resultado 

#prueba
print("cuadrados en lista sin iter:")

#creo la instancia
cuadrados = CuadradosLista()

#llama al metodo especifico
lista_completa = cuadrados.obtener_lista()

print(lista_completa)
