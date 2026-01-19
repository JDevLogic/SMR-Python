""" Ejercicio 18
Años vividos

Pide edad, calcula meses y días vividos aproximadamente """

meses = 12
dias = 365

edad = int(input("Introduce tu edad: "))

meses_total = edad * meses
dias_total = edad * dias 

print(f"Has vivido {meses_total} meses.")
print(f"Has vivido {dias_total} dias.")