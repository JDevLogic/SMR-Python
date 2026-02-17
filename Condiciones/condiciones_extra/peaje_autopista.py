"""
Ejercicio 2

Peaje de autopista.
Queremos calcular cuánto paga un vehículo al pasar por una autopista.
El programa debe pedir:
- tipo de vehículo (moto, coche, furgoneta o camión),
- kilómetros recorridos (mayor que 0),
- y la hora del paso (0–23).
Cada vehículo tiene un precio distinto por kilómetro:
- moto: 0.05 €/km
- coche: 0.08 €/km
- furgoneta: 0.10 €/km
- camión: 0.15 €/km
Además:
- en horas punta (7–9 y 17–19) el precio sube un 25%;
- si se recorren más de 200 km, hay un 10% de descuento, pero solo para coche y furgoneta.
Muestra el total y explica si se aplicó recargo y/o descuento 

"""

tipo = input("Introduce tu tipo de vehiculo (moto, coche, furgoneta o camión): ").lower()
kilometros = int(input("Introduce tus kilometros recorridos (mayor que 0): "))
hora = int(input("Introduce la hora del paso (0-23): "))

moto = 0.05 
coche = 0.08 
furgoneta = 0.10 
camion =  0.15 

recargo = 0.25
descuento = 0.10

precio_base = 0

print(f"\nElegiste el tipo de vehiculo {tipo}y recorriste {kilometros}km.\n")

if tipo == "moto":
    precio_total = moto * kilometros

elif tipo == "coche":
    precio_total = coche * kilometros

elif tipo == "furgoneta":
    precio_total = furgoneta * kilometros

elif tipo == "camion" or tipo == "camión":
    precio_total = camion * kilometros

else: 
    print("El tipo de vehiculo no valido.")
    exit()


if (hora >= 7 and hora <= 9) or (hora >= 17 and hora <= 19):
    precio_total *= (1+recargo)
    print(f"TIENES UN RECARGO EN EL PRECIO del 25%")

if kilometros > 200 and (tipo == "coche" or tipo == "furgoneta"):
    precio_total *= (1-descuento)
    print(f"TIENES UN DESCUENTO EN EL PRECIO del 10%")


print(f"\nTu precio total es de: {precio_total:.2f}€.")