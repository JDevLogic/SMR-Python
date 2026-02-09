"""Ejercicio 3

 Un ayuntamiento aplica impuestos según el valor de un vehículo. Solicita el precio del vehículo
y su tipo (gasolina, diésel, eléctrico). - Gasolina: 5% - Diésel: 8% - Eléctrico: 2% Si el precio es
superior a 30.000 €, se aplica un recargo adicional del 2%. Muestra el impuesto total y el precio
final. 

"""

precio = float(input("Introduce el precio del vehiculo: "))
tipo = input("Introduce el tipo de vehiculo (gasolina, diesel, electrico): ").lower()

if tipo == "gasolina":
    impuesto = 0.05

elif tipo == "diesel":
    impuesto = 0.08

elif tipo == "electrico":
    impuesto = 0.02

else:
    print("Tipo de vehiculo no valido. ")
    exit()

if precio > 30000:
    impuesto += 0.02

cuanto_impuesto = precio * impuesto
precio_total = precio + cuanto_impuesto

print(f"El impuesto añadido es: {cuanto_impuesto}€. ")
print(f"El precio total es: {precio_total}€. ")