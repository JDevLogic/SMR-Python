""" 
Ejercicio 13

Envío con seguro.
Una empresa de mensajería calcula el precio según varios factores.

El programa debe pedir:
- valor declarado del paquete (en €),
- peso (kg),
- franja (normal / urgente),
- si lleva seguro (sí/no).

Reglas:
- el precio base es 5 € + 1.5 € por kg;
- si es urgente, se suma un 40% sobre el precio base;
- el seguro depende del valor:
- si valor ≤ 100 → +2 €
- si 100 < valor ≤ 500 → +5 €
- si valor > 500 → +1% del valor
- si el peso es mayor de 25 kg, el envío no se admite.

Muestra el coste total y un pequeño desglose

"""

valor = int(input("Introduce el valor declarado del paquete (en €): "))
peso = float(input("Introduce el peso en kg: "))
franja = input("Introduce la franja (normal / urgente): ").lower()
seguro = input("Introduce si lleva seguro o no (si / no): ").lower().replace("í","i")


if peso > 25:
    print("El envio no se admite, porque el peso es mayor de 25kg.")
    exit()

precio_tranporte = 5 + (1.5 * peso)
recargo_urgente = 0
precio_seguro = 0

if franja == "urgente":
    recargo_urgente = precio_tranporte * 0.40
    
if seguro == "si":
    
    if valor <= 100:
        precio_seguro += 2

    elif valor <= 500:
        precio_seguro += 5
    
    elif valor > 500:
        precio_seguro =  valor * 0.01

total = precio_tranporte + recargo_urgente + precio_seguro

print(f"Precio de transporte: {precio_tranporte:.2f}€.\nPrecio recargo urgente: {recargo_urgente:.2f}€.\nPrecio del seguro: {precio_seguro:.2f}€.")
print ("-----------------------------------------------")
print(f"TOTAL: {total:.2f}€.")