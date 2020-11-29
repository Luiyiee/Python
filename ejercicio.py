
def remover_duplicados(cadenas):
    """
    Remueve los duplicados de una lista de cadenas.
    """
    no_duplicados = []

    for c in cadenas:
        if c not in no_duplicados:
            no_duplicados.append(c)
    
    return no_duplicados


lenguajes =  ['a', 'b', 'c', 'd', 'a', 'c', 'g','z','a']

print(lenguajes)

resultado = remover_duplicados(lenguajes)

print(resultado)