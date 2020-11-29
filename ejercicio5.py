def contarElementosLista(lista_contar):
    """
    Recibe una lista, y devuelve un diccionario con todas las repeticiones de
    cada valor
    """
    return {i:lista_contar.count(i) for i in lista_contar}
 
lista_A = ["a", "c", "b", "a", "c", "c", "a", "c"]
resultado=contarElementosLista(lista_A) # {'a': 3, 'b': 1, 'c': 3}
maximo=max(resultado, key=resultado.get)
print("El valor mas repetido en la lista A: ",maximo," con ",resultado[maximo]," veces")
 
 
lista_B = ["a", "h", "b", "a", "g", "c", "f", "c"]
resultado=contarElementosLista(lista_B) # {1: 2, 2: 5, 3: 2, 4: 2, 5: 1}
maximo=max(resultado, key=resultado.get)
print("El valor mas repetido en la lista B: ",maximo," con ",    resultado[maximo]," veces")