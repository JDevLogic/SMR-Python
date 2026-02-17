"""
Ejercicio 11 

Actualizar el sistema operativo (requisitos).
Un ordenador puede actualizarse si cumple ciertos requisitos.

El programa debe pedir:
- generación de CPU (entero),
- RAM en GB,
- TPM (0 o 1),
- tipo de equipo (pc / portátil).

Regla base: CPU ≥ 8, RAM ≥ 8 y TPM = 1.
Si es portátil, la RAM mínima sube a 12.

Excepción: si la CPU es generación 7, pero tienes RAM ≥ 16 y TPM = 1, se permite en “modo compatibilidad”.
El programa debe decir compatible/no compatible y explicar la primera condición que falla o si se
aplica la excepción. 

"""

generacion = int(input("Introduce la generacion de tu CPU (entero): "))
ram = int(input("Introduce tu RAM en GB: "))
tpm = int(input ("Introduce si tienes TPM  (0 / 1): "))
equipo = input("Introduce tu tipo de equipo (pc / portatil): ").lower()

cpu_base = 8
ram_base = 8
tpm_base = 1

if equipo == "portatil":
    ram_base = 12
    print("Tu equipo es un portatil por eso la ram minima sube a 12 GB. ")

else:
    ram_base = 8


    
if generacion == 7 and ram >= 16 and tpm == tpm_base:
        print(f"Tu equipo permite actualizar en ""modo compatibilidad."" ")

elif generacion < cpu_base:
    print("Tu equipo no es compatible, porque tiene una generacion CPU mas baja. ")

elif ram < ram_base:
    print("Tu equipo no es compatible, porque tienes menos RAM del minimo permitido. ")

elif tpm != tpm_base: 
    print("Tu equipo no es compatible, porque no tiene TPM. ")

else: 
    print("Tu equipo cumple con todos los requisitos. ")