"""  Ejercicio 3

Escribir un programa que pida al usuario dos números y muestre por pantalla 
su división. Si el divisor es cero el programa debe mostrar un error. """


num1 = int(input("Introduce el primer numero: \n"))
num2 = int(input("Introduce el segundo numero: \n"))

if num2 == 0:
    print("ERROR! El segundo numero no puede ser un 0.")
else:
    print(num1 / num2)