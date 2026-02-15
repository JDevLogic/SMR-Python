"""
Ejercicio 6

Triaje (prioridad sanitaria) simplificado.
En urgencias se asigna una prioridad según algunos valores.
El programa debe pedir:
- temperatura (°C),
- saturación de oxígeno (0–100),
- dolor (0–10),
- edad.
Reglas principales:
- si la saturación es menor de 90 → prioridad ROJA;
- si la temperatura es 40 o más, o el dolor es 9 o más → prioridad ROJA (si no lo era ya);
- si la saturación está entre 90 y 93, o la temperatura está entre 39 y 39.9 → prioridad AMARILLA;
- si la persona tiene 75 o más y además temperatura 38 o más, se sube un nivel (verde→amarilla,
amarilla→roja);
- si no se cumple nada de lo anterior → prioridad VERDE. 

"""

temp = float(input("Introduce tu temperatura (ºC): "))
saturacion = int(input("Introduce tu saturacion (0 - 100)%: "))
dolor = int(input("Introduce tu nivel de dolor (0 - 10 ): "))
edad = int(input("Introduce tu edad: "))

prioridad = "VERDE"
motivo = "No se cumplio ninguna de las condiciones."

if saturacion < 90:
    prioridad = "ROJA"
    motivo = "La saturación es menor de 90%."

elif temp >= 40 or dolor >= 9:
    prioridad = "ROJA"
    motivo = "La temperatura es 40 o más, o el dolor es 9 o más."

elif (saturacion >= 90 and saturacion <= 93) or (temp >= 39 and temp <= 39.9):
    prioridad = "AMARILLA"
    motivo = "La saturación está entre 90 y 93, o la temperatura está entre 39 y 39.9."

if edad >= 75 and temp >= 38:
    if prioridad == "VERDE":
        prioridad = "AMARILLA"
        motivo = "La persona tiene 75 o más y además temperatura 38 o más, se sube un nivel (verde->amarilla)."

    elif prioridad == "AMARILLA":
        prioridad = "ROJA"
        motivo = "La persona tiene 75 o más y además temperatura 38 o más, se sube un nivel (amarilla->roja)."

print(f"\nSegun los datos su prioridad es de color: {prioridad}.")
print(f"MOTIVO: {motivo}")
