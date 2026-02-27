""" 
Ejercicio 14 

Asignación de aula.
Hay tres aulas disponibles y hay que asignar la “más pequeña” que cumpla requisitos.

El programa debe pedir:
- número de alumnos,
- si hace falta accesibilidad (sí/no),
- si hace falta que haya PCs (sí/no).

Aulas:
- Aula A: capacidad 20, accesible sí, PCs no
- Aula B: capacidad 30, accesible no, PCs sí
- Aula C: capacidad 25, accesible sí, PCs sí

Regla: elige la más pequeña que cumpla TODO lo que se pide.
Si ninguna vale, di “no asignable” y explica qué requisito falla (capacidad, accesibilidad o PCs).
Hazlo solo con condicionales (sin listas ni bucles) 

"""

alumnos = int(input("Introduce el numero de alumnos: "))
accesibilidad = input("Introduce si hace falta accesibilidad o no (si / no): ").lower().replace("í","i")
falta_pcs = input("Introduce si hace falta PCs o no (si / no): ").lower().replace("í","i")

if alumnos <= 20 and accesibilidad == "si" and falta_pcs == "no":
    print("Asignada Aula A.")

elif alumnos <= 25 and accesibilidad == "si" and falta_pcs == "si":
    print("Asignada Aula C.")

elif alumnos <= 30 and accesibilidad == "no" and falta_pcs == "si":
    print("Asignada Aula B.")

else:
    print("No asignable.")
    
    if alumnos > 30: 
        print("Te pasaste de la capacidad de las aulas.")
    
    elif accesibilidad == "si" and alumnos > 25:
        print("El requisito de accesibilidad falló. ")
    
    elif falta_pcs == "si" and alumnos > 30:
        print("El requisito de falta de PCs falló. ")
