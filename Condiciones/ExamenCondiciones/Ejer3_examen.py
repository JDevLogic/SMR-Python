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
- una explicación breve del motivo principal 

"""

import random

edad_paciente = int(input("Introduce la edad del paciente: "))
temperatura = float (input("Introduce la temperatura corporal del paciente: "))
saturacion = int (input("Introduce la saturacion del paciente (0 - 100): "))
dolor = int (input("Introduce el nivel de dolor del paciente (0 - 10): "))

dificultad_respiratoria = True
enfermedad_grave = True
paciente_caminando = False

alerta_hospital = random.randint(0,1)
box_critico = random.randint(0,1)

subida_escalado = False
motivo = ""

if (saturacion < 0 or saturacion > 100) or (dolor < 0 or dolor > 10) or (temperatura < 30 or temperatura >45):
    print("Datos no validos")
    exit()

if saturacion < 90 or (dificultad_respiratoria and saturacion < 94) or (temperatura >= 40 and dolor >= 8):
    prioridad = "ROJA"
    motivo = "Saturacion menor de 90 o tienes dificultad respiratoria y tu saturacion es menor de 94 o tu temperatura es mayor o igual a 40 y tu dolor es mayor o igual a 8. "
elif (saturacion >= 90 and saturacion <= 93) or (temperatura >= 39 and temperatura<= 39.9) or (dolor >= 7 and dolor <= 8):
    prioridad = "AMARILLA"
    motivo = "Saturacion esta entre 90 y 93 o tu temperatura esta entre 39 y 39.9 o tu dolor esta entre 7 y 8."
else:
    prioridad = "VERDE"
    motivo = "Cualquier otro caso."


if edad_paciente >= 75 and (temperatura >= 38 or enfermedad_grave):
    if prioridad == "VERDE":
        prioridad = "AMARILLA"
    elif prioridad == "AMARILLA":
        prioridad = "ROJA"
    motivo = "Se sube de nivel porque tienes 75 y tu temperatura es de 38 o mas o tienes una enfermedad grave."
    subida_escalado = True

if not paciente_caminando and (dolor >= 6 or dificultad_respiratoria):
    if prioridad == "VERDE":
        prioridad = "AMARILLA"
    elif prioridad == "AMARILLA":
        prioridad = "ROJA"
    motivo = "Se sube de nivel porque no puedes caminar y tienes dolor 6 o mas o tienes dificultad respiratoria."
    subida_escalado = True

if edad_paciente < 12:
    if temperatura >= 39 and dificultad_respiratoria:
        prioridad = "ROJA"
        motivo = "Porque eres menor de 12 años y tienes 39 o mas de temperatura y tienes dificultad respiratoria."
    elif dolor >= 8:
        if prioridad == "VERDE":
            prioridad = "AMARILLA"
            motivo = "Se sube de nivel del verde al amarillo, porque eres menor de 12 años y tienes dolor 8 o mas."
    
    if enfermedad_grave:
        if prioridad == "VERDE":
            prioridad = "AMARILLA"
        elif prioridad == "AMARILLA":
            prioridad = "ROJA"
        motivo = "Se sube de nivel, porque eres menor de 12 años y tienes enfermedad grave."

if alerta_hospital == 1 and prioridad == "AMARILLA" and (enfermedad_grave or edad_paciente >= 75):
    prioridad = "ROJA"
    motivo = "Hay una alerta hospitalaria y tu prioridad era amarilla y tienes una enfermedad grave o tu edad es de 75 o mas."

if box_critico == 0 and prioridad == "ROJA" and subida_escalado:
    if saturacion >= 95 and temperatura < 38 and dolor <= 5:
        prioridad = "AMARILLA"
        motivo = "Se baja de nivel porque no hay box critico y tu subida de nivel fue por solo edad o por no poder caminar."

print(f"PRIORIDAD: {prioridad}\nMOTIVO: {motivo}")