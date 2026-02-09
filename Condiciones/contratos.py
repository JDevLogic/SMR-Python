""" 
Ejercicio 1 

Una empresa ofrece distintos contratos según la edad y la experiencia. Solicita la edad y los
años de experiencia laboral. - Si es menor de 18, no puede ser contratado. - Si tiene entre 18 y
21 y menos de 1 año de experiencia, se ofrece contrato de prácticas. - Si tiene más de 21 y al
menos 2 años de experiencia, se ofrece contrato indefinido. - En cualquier otro caso, contrato
temporal. Muestra el tipo de contrato resultante. 

"""

edad = int (input("Introduce tu edad: "))

experiencia_year = int (input("Introduce tu experiencia en años: "))
experiencia_meses = int (input("Introduce tu experiencia en meses: "))

total_meses = experiencia_year * 12 + experiencia_meses

if edad < 18:
    print("No puedes ser contratado, porque eres menor de edad. ")

elif (edad >= 18 and edad <= 21) and total_meses < 12:
    print("Te ofrecemos un contrato de practicas. ")

elif edad > 21 and total_meses >=24:
    print("Te ofrecemos contrato indefinido. ")

else:
    print("Contrato temporal.")

