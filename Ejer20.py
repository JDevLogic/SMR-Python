""" Ejercicio 20
Programa completo final

Pide nombre, edad, horas estudio/semana. Calcula horas/mes y /año """
sem_mes = 4
sem_year = 52

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
horas_semana = float(input("Cuantas horas semanales estudiaste? "))

horas_mes = horas_semana * sem_mes
horas_year = horas_semana * sem_year

print(f"\nNombre: {nombre}.\nEdad: {edad}.\nLas horas de estudio al mes son: {horas_mes}.\nLas horas de estudio al año son: {horas_year}.")