"""  Ejercicio 13
Calculadora de sueldo
Pide horas trabajadas y precio/hora, calcula sueldo total """

horas = float(input("Introduce en horas lo que has trabajado: "))
precio_hora = float(input("Introduce el precio/hora: "))

sueldo = horas * precio_hora

print(f"Tu sueldo es de: {sueldo}€.")