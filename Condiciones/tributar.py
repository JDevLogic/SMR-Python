""" Ejercicio 5

Para tributar un determinado impuesto se debe ser mayor de 16 años 
y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y
sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no. """

edad = int(input("Introduce tu edad: \n"))

ing_men = float (input("Introduce tus ingresos mensuales: \n"))

if edad > 16 and ing_men >= 1000:
    print("El usuario cumple con los requisitos tiene que tributar.")

elif edad > 16 or ing_men >= 1000:
    print("El usuario cumple solo con uno de los 2 requisitos.")

else:
    print("El usuario no cumple con ningun requisito.")