arreglo = ([55, 21, 19, 11,  9])

for recorrido in range(1, len(arreglo)):
    for position in range(len(arreglo) - recorrido):
        if arreglo[position] > arreglo[position + 1]:
            temp = arreglo[position]
            arreglo[position] = arreglo[position + 1]
            arreglo[position + 1] = temp
print(arreglo)