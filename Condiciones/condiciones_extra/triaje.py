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

