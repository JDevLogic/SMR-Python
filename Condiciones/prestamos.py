""" 
Ejercicio 7 

Un banco concede préstamos según salario y estabilidad laboral. Solicita salario mensual y
tipo de contrato (temporal o indefinido). - Salario < 1200: préstamo denegado. - Salario entre
1200 y 2000 con contrato temporal: préstamo denegado. - Salario ≥ 2000 o contrato indefinido:
préstamo aprobado. Muestra el resultado. 

"""

salario = int(input("Introduce tu salario mensual: "))
contrato = input("Introduce tu tipo de contrato: ").lower()

if salario < 1200:
    print(f"PRESTAMO DENEGADO\nPorque tu salario es menor a 1200. ")

elif salario >= 1200 and salario < 2000 and contrato == "temporal":
    print(f"PRESTAMO DENEGADO\nPorque tienes entre 1200 y 2000 y un contrato temporal. ")

elif salario >= 2000 or contrato == "indefinido":
    print(f"PRESTAMO CONCEDIDO\nPorque tienes cobras al menos 2000€ o tienes contrato indefinido. ")

else:
    print("Los tipos de contratos son: temporal o indefinido")