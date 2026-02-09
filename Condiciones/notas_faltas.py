""" 
    Ejercicio 4 
Un centro educativo evalúa la promoción del alumnado. Solicita tres notas y el número de
faltas.
    - Si alguna nota es inferior a 3, suspende directamente. 
    - Si la media es inferior a 5,suspende. 
    - Si la media es mayor o igual a 5 pero las faltas superan 20, suspende. 
    - Encualquier otro caso, aprueba. Muestra el resultado final.
"""

n1 = int(input("Introduzca la primera nota: "))
n2 = int(input("Introduzca la segunda nota: "))
n3 = int(input("Introduzca la tercera nota: "))

faltas = int(input("Introduce tus faltas: "))

media_notas= (n1+ n2 + n3) / 3

print(media_notas)

if(n1 < 3 and n2 < 3 and n3 <3 ):
    print("Suspendido")
elif(n1<5 and n2 <5 and n3 <5):
    print("Notas suspendido.")
elif(n1>=5 and n2 >= 5 and n3 >= 5):
    if(faltas<20):
        print("Suspendido por faltas. ")
    else:
        print("Aprobado.")