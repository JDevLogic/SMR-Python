"""
Ejercicio 7

Cálculo de nómina (muy aproximado).
Se quiere estimar el neto mensual aplicando una retención por tramos y un posible plus.
El programa debe pedir:
- salario bruto mensual,
- tipo de contrato (temporal / indefinido),
- y si trabaja de noche (sí/no).
Tramos de retención:
- hasta 1400 € → 8%
- de 1400.01 a 2200 € → 12%
- más de 2200 € → 16%
Plus de nocturnidad: +80 €, pero solo si el contrato es indefinido.
Ojo con esta excepción: si el contrato es temporal y el bruto es menor de 1200 €, la retención mínima
será 6% (aunque por tramo te saliera menos).
Muestra bruto, retención en euros, neto y una frase explicando qué reglas se aplicaron. 

"""

salario = float(input("Introduce tu salario bruto mensual: "))
contrato = input("Introduce tu tipo de contrato (indefinido / temporal): ").lower()
nocturnidad = input("Introduce si trabajas de noche o no (si / no)").lower()

porcentaje = 0

if salario <= 1400:
    porcentaje = 0.08
    print(f"\nSe aplica el 8% de retencion, porque tu salario es de hasta 1400€.")

elif salario < 2200:
    porcentaje = 0.12
    print(f"\nSe aplica el 12% de retencion, porque tu salario es de 1400.01 a 2200 €. ")

else:
    porcentaje = 0.16
    print(f"\nSe aplica el 16% de retencion, porque tu salario es más de 2200 €. ")

if contrato == "temporal" and salario < 1200:
    porcentaje = 0.06
    print(f"\nSe aplica el 6% de retencion, porque tu contrato es temporal y el bruto es menor de 1200 €. ")


retencion = salario * porcentaje
salario_neto = salario - retencion

if contrato == "indefinido" and nocturnidad == "si":
    salario_neto =  salario_neto + 80
    print(f"Se aplica el plus de nocturnidad, porque trabajas de noche y tu contrato es indefinido.\n ")


print(f"\nTu salario bruto es de: {salario}€.")
print(f"Tu retencion es de: {retencion}€.")
print(f"Tu salario neto es de: {salario_neto}€.\n")