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
anual = input("Introduce si el pago es anual o no (si / no): ")

precio_basic = 7.99
precio_standart = 11.99
precio_premium = 15.99

maximo_disp = 0

if plan == "basico":
    maximo_disp = 1

elif plan == "standart":
    maximo_disp = 2

elif plan == "premium":
    maximo_disp = 4
else:
    print("El plan no existe. ")
    exit()

if dispositivos > maximo_disp:
    print(f"Supera el máximo del plan {plan}.")
    exit()
else:
    
    if plan == "basico":
        precio = precio_basic
        
    elif plan == "standart":
        precio = precio_standart

    elif plan == "premium":
        precio = precio_premium

    
    if anual == "si":
        precio_anual = precio * 10
        print(f"PRECIO ANUAL\nEl precio anual a pagar es de: {precio_anual}€.")
    
    else:
        print (f"PRECIO MENSUAL\nEl precio mensual a pagar es de: {precio}€.") 