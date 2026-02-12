""" Ejercicio 9

Una tienda online aplica descuentos: Solicita el total de la compra y si el cliente es socio. -
Compras < 50 €: sin descuento. - Entre 50 y 150 €: 5%. - Más de 150 €: 10%. Los socios
obtienen un 5% adicional. Muestra el precio final. 

"""

compra = int(input("Introduce el total de la compra: "))
socio = input("Introduce si eres socio (si/no): ").lower()

porcentaje_descuento = 0

if compra <50:
    porcentaje_descuento = 0

elif compra >=50 and compra <=150:
    porcentaje_descuento += 0.05

elif compra >150:
    porcentaje_descuento += 0.10
    
if socio == "si":
    porcentaje_descuento += 0.05

descuento = compra * porcentaje_descuento
total_compra = compra - descuento
descu = porcentaje_descuento * 100 

print(f"Recibes el {descu}% de descuento")
print(f"Tu total de la compra seria: de {total_compra}")