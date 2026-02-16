""" 
Ejercicio 9 

Cancelación de hotel.
Un hotel aplica penalización dependiendo de cuándo cancelas y del tipo de tarifa.

El programa debe pedir:
- días que faltan para la llegada,
- tipo de tarifa (flexible / no_reembolsable),
- temporada (baja / alta).

Reglas:
- si la tarifa es no_reembolsable, la penalización es del 100% siempre;
- si es flexible: con 7 días o más -> 0%, entre 3 y 6 -> 30%, y si faltan menos de 3 -> 70%;
- si es temporada alta, a la penalización se le suman 10 puntos (sin pasar de 100%).

Muestra el % final y explica por qué.

"""


llegada = int(input("Introduce cuantos dias faltan para tu llegada: "))
tarifa = input("Introduce tu tipo de tarifa (flexible / no reembolsable): ").lower() 
temporada = input("Introduce si que temporada estas (baja / alta): ").lower()

porcentaje = 0

if tarifa == "no reembolsable":
    porcentaje = 100
    print(f"\nTu porcentaje es de: {porcentaje}%, porque tu tarifa es no reembolsable")

else:
    if llegada >= 7:
        porcentaje = 0
        print(f"\nTu porcentaje es de: {porcentaje}%, porque faltan 7 o mas dias para tu llegada ")
    
    elif llegada >= 3 and llegada <= 6:
        porcentaje = 30
        print(f"\nTu porcentaje es de: {porcentaje}%, porque faltan  entre 3 y 6 dias para tu llegada ")
    
    else:
        porcentaje = 70
        print(f"\nTu porcentaje es de: {porcentaje}%, porque faltan menos de 3 dias para tu llegada ")


    if temporada == "alta":
        porcentaje = porcentaje + 10 
        if porcentaje > 100:
            porcentaje = 100
            print(f"Tu porcentaje es de: {porcentaje}%, porque no puede superar el 100%. ")
        
        print(f"Tu porcentaje es de: {porcentaje}%, porque es temporada alta y se suma 10 puntos. ")
          


        
