""" Ejercicio 3 — Sistema de triaje hospitalario (5)

En el servicio de urgencias de un hospital se utiliza un sistema de triaje para decidir qué pacientes deben ser atendidos
antes según la gravedad de su estado. El programa debe determinar una prioridad final para cada paciente.

El programa debe pedir:
- edad del paciente
- temperatura corporal
- saturación de oxígeno (0–100)
- nivel de dolor (0–10)
- dificultad respiratoria (bool)
- enfermedad grave previa (bool)
- si el paciente llegó caminando (bool)

Además, el hospital puede encontrarse en situaciones especiales que afectan al sistema de decisión:
- alerta hospitalaria: elegir aleatoriamente 0 o 1
- box crítico libre: elegir aleatoriamente 0 o 1

Asignación de prioridad base:

- prioridad ROJA si:
• saturación < 90
• dificultad respiratoria y saturación < 94
• temperatura ≥ 40 y dolor ≥ 8

- prioridad AMARILLA si no era roja y:
• saturación entre 90 y 93
• temperatura entre 39 y 39.9
• dolor entre 7 y 8

- en cualquier otro caso → prioridad VERDE

Escalado de prioridad:
- subir un nivel si edad ≥ 75 y (temperatura ≥ 38 o enfermedad grave)
- subir un nivel si el paciente no llegó caminando y (dolor ≥ 6 o dificultad respiratoria)

Caso especial para menores de 12 años:
- si temperatura ≥ 39 y dificultad respiratoria → prioridad ROJA
- si no, pero dolor ≥ 8 → al menos AMARILLA
- si además tiene enfermedad grave → subir otro nivel

Situaciones del hospital:
- si hay alerta hospitalaria (1) y la prioridad era AMARILLA y además el paciente tiene enfermedad grave o edad ≥ 75 →
subir a ROJA
- si no hay box crítico libre (0) y la prioridad había subido solo por edad o por no caminar, puede bajarse de ROJA a
AMARILLA si:
• saturación ≥ 95
• temperatura < 38
• dolor ≤ 5

El programa debe mostrar:
- la prioridad final del paciente (VERDE / AMARILLA / ROJA)
- una explicación breve del motivo principa 

"""

import random

edad_paciente = int(input("Introduce la edad del paciente: "))
temperatura = float (input("Introduce la temperatura corporal del paciente: "))
saturación = int (input("Introduce la saturacion del paciente (0 - 100): "))
dolor = int (input("Introduce el nivel de dolor del paciente (0 - 10): "))

dificultad_respiratoria = True
enfermedad_previa = True
paciente_caminando = True

alerta_hospital = random.randint(0,1)
box_critico = random.randint(0,1)


if saturacion < 0 or saturacion > 100 or dolor < 0 or dolor > 10 or temperatura < 30 or temperatura >45:
    print("Datos no validos")
else:
    if saturacion < 90 or (dificultad and saturacion < 94) or (temperatura >= 40 and dolor >= 8):
        prioridad = "ROJA"
    elif saturacion >= 90 and saturacion <= 93 or temperatura >= 39 and temp <= 39.9 or dolor >= 7 and dolor <= 8:
        prioridad = "AMARILLA"
    else:
        prioridad = "VERDE"





