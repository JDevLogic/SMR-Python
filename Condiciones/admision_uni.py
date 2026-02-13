""" 
Ejercicio 10 

Un sistema de admisión universitaria evalúa candidatos. Solicita nota media y si ha superado
la prueba específica. - Nota < 5: rechazado. - Nota entre 5 y 6.9 sin prueba: rechazado. - Nota
≥ 7 o prueba superada: admitido. Muestra el resultado 

"""

nota_media = float (input("Introduce tu nota media: "))
prueba = input("Introduce si has superado la prueba especifica o no (si / no): ").lower()

if nota_media < 5:
    print("RECHAZADO\nPorque tienes la nota media menos de 5.")

elif nota_media >= 7 or prueba == "si":
    print("APROBASTE\nPorque sacaste de nota 7 o mas, o superaste la prueba especifica.")

elif nota_media >= 5 and nota_media <=6.9:
    if prueba == "no":
        print("RECHAZADO\nPorque no has superado la prueba especifica")

