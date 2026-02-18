"""
Ejercicio 10 

Beca de transporte.
Se quiere decidir si se concede una beca y de cuánto.

El programa debe pedir:
- distancia desde casa (km),
- ingresos mensuales,
- modalidad (bus / tren / coche_compartido).

Reglas:
- si la distancia es menor de 5 km → no hay beca;
- el umbral de ingresos base es 1600 €;
- si la modalidad es tren, el umbral sube 200 €;
- si la modalidad es coche_compartido, solo se permite si la distancia es 15 km o más.

Cuantía según distancia:
- 5–14 km: 25 €
- 15–29 km: 45 €
- 30 km o más: 65 €

Solo se concede si ingresos ≤ umbral calculado.
Muestra si se concede, la cuantía y el motivo. 

"""

distancia = int(input("Introduce la distancia desde tu casa (km): "))
ingresos = int(input("Introduce tus ingresos mensuales: "))
modalidad = input("Introduce la modalidad (bus / tren / coche compartido): ").lower()

umbral = 1600
cuantia = 0

if distancia < 5:
    print("\nNo tienes beca, porque la distancia es menos de 5 km.")
    exit()

elif modalidad == "coche compartido" and distancia < 15:
    print("\nNo se permite beca porque tienes coche compartido y tu distancia desde casa es menor a 15km. ") 
    exit()


if modalidad == "tren":
        umbral= umbral + 200
        print("El umbral se suma 200€, porque tu modalidad es tren")
    
if ingresos <= umbral:
    print("\nLa beca se concede.")
        
    if distancia >= 5 and distancia <= 14:
        cuantia = 25
        print(f"Tu cuantia es de: {cuantia}€, porque la distancia es de 5-14km.")
        
    elif distancia >= 15 and distancia <= 29:
        cuantia = 45
        print(f"Tu cuantia es de: {cuantia}€, porque la distancia es de 15-29km.")
        
    else:
        cuantia = 65
        print(f"Tu cuantia es de: {cuantia}€, porque la distancia es mayor a 30 km.")
    
else:
    print("\nLa beca no se concede, porque tus ingresos son mayores que el umbral.")