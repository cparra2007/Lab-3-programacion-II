print("contador 10-15 con next:")

numeros_iterable = range(10, 16)
#iter para tomar el objeto y delvolver el iterador

mi_iterador = iter(numeros_iterable)

#recorrer el iterador usando next
try:
    print(next(mi_iterador)) 
    print(next(mi_iterador)) 
    print(next(mi_iterador)) 
    print(next(mi_iterador)) 
    print(next(mi_iterador)) 
    print(next(mi_iterador)) 
except StopIteration:
    print("Se han agotado los elementos.")
