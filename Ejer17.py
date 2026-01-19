""" Ejercicio 17
Ticket de compra

Pide precio de 3 productos, muestra total, IVA y total con IVA """

producto1 = int(input("Introduce el precio del primer producto: "))
producto2 = int(input("Introduce el precio del segundo producto: "))
producto3 = int(input("Introduce el precio del tercer producto: "))

iva = 21

productos_total = producto1 + producto2 + producto3

iva_total = productos_total * (iva/100)

precio_total = productos_total + iva_total

print(f"El precio total de los 3 productos es {productos_total}€.")
print(f"El precio del IVA es de {iva_total}€.")
print(f"El precio total con IVA incluido es de {precio_total}€.")