""" 
Ejercicio 5 

Suscripción de streaming.
Una plataforma tiene tres planes y cada uno limita el número de dispositivos.
El programa debe pedir:
- plan (basic / standard / premium),
- número de dispositivos (1–6),
- y si el pago es anual (sí/no).
Reglas de dispositivos:
- basic: máximo 1
- standard: máximo 2
- premium: máximo 4
Si se supera el máximo del plan, se muestra un error y no se calcula el precio.
Precios mensuales:
- basic: 7.99 €
- standard: 11.99 €
- premium: 15.99 €
Si el pago es anual, se descuentan 2 meses (equivale a pagar 10 meses).
Muestra el coste (mensual o anual) y explica el cálculo 

"""


plan = input("Introduce tu plan (basic / standard / premium): ").lower()
dispositivos = int(input("Introduce el numero de dispositivos: "))
anual = input("Introduce si el pago es anual o no (si / no): ").lower().replace("í","i")

precio = 0

if plan == "basico" and dispositivos > 1:
    print(f"Supera el máximo del plan {plan}.")
    exit()

elif plan == "standart"and dispositivos > 2:
    print(f"Supera el máximo del plan {plan}.")
    exit()

elif plan == "premium"and dispositivos >4:
    print(f"Supera el máximo del plan {plan}.")
    exit()   

if plan == "basico":
        precio = 7.99
        
elif plan == "standart":
        precio = 11.99

elif plan == "premium":
        precio = 15.99

else:
    print("El plan no existe.")
    exit()

if anual == "si":
    print(f"PRECIO ANUAL\nEl precio anual a pagar es de: {precio * 10}€.")
   
else:
    print (f"PRECIO MENSUAL\nEl precio mensual a pagar es de: {precio}€.") 