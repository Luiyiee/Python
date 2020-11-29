
import numpy as np 

arregloA=['A']

arregloR=['R']
arreglo = np.array([8.75, 8.46, 4.98, 5.21, 5.53, 4.52, 5.35, 6.86, 6.15, 8.76, 5.75])
print("Aprobados")
for n in range(len(arreglo)):
    # print(n+1,":", arregloA[n])
    if  arreglo[n] >= 5.75:
        # n+1,":", arregloA[n]
      
        newArray = np.append(arregloA, arreglo[n])

        print( newArray)
print()
print("Reprobados")
for n in range(len(arreglo)):
    # print(n+1,":", arregloA[n])
    if  arreglo[n] < 5.75:
        # n+1,":", arregloA[n]
      
        newArray = np.append(arregloR, arreglo[n])
       
        print( newArray)
   
