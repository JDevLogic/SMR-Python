""" 
Ejercicio 4

Control de calidad de un alimento.
Se quiere comprobar si un producto es apto para el consumo.
El programa debe pedir:
- temperatura de conservación (en °C),
- cuántas horas ha estado fuera de la nevera,
- y si el envase estaba sellado (sí/no).
Reglas:
- si el envase no estaba sellado y estuvo fuera más de 2 horas → NO apto;
- si la temperatura es mayor de 8°C y estuvo fuera más de 1 hora → NO apto;
- si la temperatura está entre 5°C y 8°C (incluidos) y estuvo fuera más de 4 horas → NO apto;
- en cualquier otro caso → apto.
El programa debe decir “apto” o “no apto” y señalar qué regla ha sido la que manda.

"""

temperatura = int(input("Introduce la temperatura de conservación (en °C): "))
horas = int(input("Introduce las horas que ha estado fuera de la nevera: "))
sellado = input("Introduce si el envase estaba sellado (sí / no): ").lower().replace("í","i")

if sellado == "no" and horas > 2:
    print("\nNO APTO\nPorque no estaba sellado y estuvo fuera mas de 2 horas.")

elif temperatura >8 and horas > 1:
    print("\nNO APTO\nPorque su temperatura es mayor a 8ºC y estuvo fuera más de 1 hora")

elif (temperatura >= 5 and temperatura <= 8) and horas > 4:
    print("\nNO APTO\nPorque la temperatura esta entre 5°C y 8°C (incluidos) y estuvo fuera más de 4 horas")
    
else:
    print("\nAPTO\nPorque no se ha incumplido ninguna regla para su consumo. ")