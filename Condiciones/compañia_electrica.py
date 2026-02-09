""" Ejercicio 5

Una compañía eléctrica calcula la factura según consumo mensual: - Hasta 100 kWh: 0.10
€/kWh - De 101 a 300 kWh: 0.15 €/kWh - Más de 300 kWh: 0.20 €/kWh Si el consumo supera
500 kWh, se aplica un recargo fijo de 30 €. Muestra el coste total. 

"""

consumo = float(input("Introduce el consumo mensual en kWh: "))

if consumo <= 100: 
    precio = consumo * 0.10

elif consumo <= 300: 
    precio = consumo * 0.15

else:
    precio = consumo * 0.20

if consumo > 500:
    precio += 30

print(f"El total de la factura es: {precio}")
