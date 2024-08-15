#programa que devuelve numeros de 1 a 10 de forma aleatoria y que no se repite ningun numero por ejemplo no puede haber 2 y 2 

import random   

n=int(input("Introduce la cantidad de veces que quieres que salga el numero: "))

for i in range(n): 
    print(random.randint(1,10))

    

    
