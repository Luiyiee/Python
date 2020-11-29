def has_duplicates(lista):
    return len(lista) != len(set(lista))
 
def values_duplicated(lista):
    return list(set([k for k in lista if lista.count(k)>1]))
 
lista1 = [1,2,3,2,4,5,3]
lista2 = [1,2,3,4,5]
 
print(has_duplicates(lista1)) # true
print(has_duplicates(lista2)) # false
 
print(values_duplicated(lista1)) # [2, 3]
print(values_duplicated(lista2)) 