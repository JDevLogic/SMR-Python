""" Ejercicio 6

Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la "M" 
y los hombres con un nombre posterior a la "N" y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo,
y muestre por pantalla el grupo que le corresponde. """

genero = input("Introduce tu genero: \n")

nombre = input("Introduzca su nombre: \n")

letra = nombre[0]

if genero.upper() == "MUJER" and letra.upper() < "M":
    print("Perteneces al grupo A.")

elif genero.upper() == "HOMBRE" and letra.upper() > "N":
    print("Perteneces al grupo A.")

else:
    print("Perteneces al grupo B")