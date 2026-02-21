""" 
Ejercicio 12

Nota con penalización por faltas.
Se quiere calcular la nota final aplicando penalización por faltas de ortografía.

El programa debe pedir:
- nota base (0–10),
- número de faltas,
- si es examen oficial (sí/no).

Reglas:
- la penalización normal es 0.1 por falta;
- si es oficial, a partir de 10 faltas la penalización pasa a 0.2 por falta;
- la nota final nunca puede ser menor que 0;
- excepción: si la nota final queda por debajo de 5, pero la nota base era al menos 5 y hay 3 faltas o menos, se aprueba “por criterio del centro”.
Muestra la nota final (con 2 decimales), aprobado/suspenso y la regla que ha decidido. 

"""

nota = float(input("Introduce tu nota base (0-10): "))
faltas = int(input("Introduce tu numero de faltas :  "))
oficial = input("Introduce si el examen es oficial o no (si / no): ").lower().replace("í","i")

penalizacion = 0.1
penalizacion_motivo = "Tu penalizacion es normal de 0.1 por falta."
estado = ""
decision = ""

if oficial == "si" and faltas >= 10:
    penalizacion = 0.2
    penalizacion_motivo = "A partir de 10 faltas la penalizacion pasa a 0.2 por falta."

penalizacion_faltas = faltas * penalizacion
nota_final = nota - penalizacion_faltas

if nota_final < 0:
    nota_final = 0

if nota_final >=5:
    estado = "APROBADO"
    decision = "Aprobado porque la nota final es 5 o superior."

else:
    estado = "SUSPENDIDO"
    decision = "Suspendido porque la nota final es inferior a 5."
    
    if nota >= 5 and faltas <= 3:
        estado = "APROBADO"
        decision = "Por criterio del centro, porque la nota final queda por debajo de 5, pero la nota base era al menos 5 y hay 3 faltas o menos."

print(f"\n{estado}.\nTu nota final es de: {nota_final:.2f}.\n{decision}\n{penalizacion_motivo}")