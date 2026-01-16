"""  Ejercicio 9
Calculadora simple
Pide dos números, muestra suma, resta y multiplicación """



num1 = int(input("Introduzca el primero numero: "))
num2 = int(input("Introduzca el segundo numero: "))

numeros_sumados = num1 + num2
numeros_restados = num1 - num2
numeros_multiplicados = num1 * num2

print(f"El resultado de la suma es: {numeros_sumados}.\nEl resultado de la resta es: {numeros_restados}.\nEl resultado de la multiplicacion es: {numeros_multiplicados}.")