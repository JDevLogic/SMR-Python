"""
Ejercicio 6 

Un sistema de alquiler de coches decide si un cliente puede alquilar: Solicita edad, años de
carnet y si tiene tarjeta de crédito. - Menor de 21: no puede alquilar. - Entre 21 y 24: necesita al
menos 2 años de carnet. - A partir de 25: basta con 1 año de carnet. En todos los casos es
obligatoria la tarjeta de crédito. Muestra si puede alquilar o no y el motivo. 

"""

edad = int (input("Introduce tu edad: "))
carnet = int (input("Introduce tus años de carnet: "))
credito = input(f"Tienes tarjeta de credito?\n").lower()

if credito == "si":
    if edad < 21:
        print("No puedes alquilar, porque tienes menos de 21 años.")
    
    elif edad >= 21 and edad <=24:
        if carnet >= 2:
            print("Puedes alquilar un coche, porque tienes entre 21 y 24 y tienes al menos 2 años de carnet")
        else:
            print("No puedes alquilar coche, porque no tienes al menos 2 años de carnet.")
    
    elif edad >= 25:
        if carnet >= 1:
            print("Puedes alquilar un coche, porque tienes a partir de 25 y al menos 1 año de carnet.")
        else:
            print("No puedes alquilar un coche, porque no tienes al menos un año de carnet")

elif credito == "no":
    print("No puedes alquilar un coche, porque no tienes tarjeta de credito.")

else:
    print("Escribe si tienes tarjeta de credito con Si o No.")