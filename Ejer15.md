Ejercicio 15

Analiza el programa

Encuentra el error en un código dado y explícalo

## Ejercicio analizado: Ejer4.py

### Codigo del ejercicio:

```python

"""  Ejercicio 4
Operaciones básicas
Crea dos números y muestra suma, resta, multiplicación y división """

num1 = 10

num2 = 5

num_sumado = num1 + num2

num_restado = num1 + num2

num_multiplicado = num1 * num2

num_dividido = num1 / num2

print(f"El resultado de la suma es: {num_sumado}")
print(f"El resultado de la resta es: {num_restado}")
print(f"El resultado de la multiplicacion es: {num_multiplicado}")
print(f"El resultado de la division es: {num_dividido}")

```

### Error identificado:
Division por cero(ZeroDivisionError)

### Que es el ZeroDivisionError:
Si el valor de num2 es 0 ocurre porque cuando se intenta dividir un numero entre 0. En matemáticas, la división por cero no está definida. Python detecta esta operación inválida y lanza este error deteniendo el programa.