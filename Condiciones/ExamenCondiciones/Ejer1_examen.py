""" 
Ejercicio 1 
Sala de estudio 

Pide: edad
tipo (alumno/profesor/externo) 
hora (0–23)
ocupación (0–100)
reserva (bool: True/False)

Reglas:
- hora u ocupación inválidas → Datos no válidos
- ocupación = 100 → no entra nadie
- ocupación ≥ 90 → solo profesor o reserva = True
- externo solo entra de 10 a 18
- menor de 16: externo no entra; alumno solo 10–17
- de 20 a 23: alumno solo con reserva = True

Muestra: acceso permitido / denegado + motivo
 
"""

edad = int(input("Introduce tu edad: "))
tipo = input("Introduce que tipo eres (alumno/profesor/externo): ").strip().lower()
hora = int(input("Introduce la hora (0–23): "))
ocupacion = int(input("Introduce el porcentaje de ocupacion (0 - 100): "))
reserva = True


if hora < 0 or hora >23 or ocupacion < 0 or ocupacion >100:
    print("Datos no validos.")
    exit()

if ocupacion == 100:
    print("Acceso denegado, porque la ocupacion es del 100%. ")
    exit()

if ocupacion >= 90:
    if tipo == "profesor" or reserva:
        print("Acceso permitido, la ocupacion es del 90% o mas, eres profesor o tienes reserva.")

else:
    if edad > 16:
        if tipo == "externo":
            print("Acceso denegado, porque eres externo y tienes menos de 16 años.")
            exit()
        elif tipo == "alumno":
            if hora >= 10 and hora <= 17:
                (print("Acceso permitido, eres alumno tienes menos de 16 años y tu hora es 10 a 17"))
            else:
                (print("Acceso denegado, eres alumno tienes menos de 16 años y no estas en la hora de 10 a 17"))
    
    elif edad >= 20 and edad <= 23:
        if tipo == "alumno" and reserva:
            print("Acceso permitido, porque eres alumno y tienes reserva.")             

    if tipo == "externo":
        if hora >= 10 and hora <= 18:
            print("Acceso permitido, eres externo y has entrado entre las 10 y 18.")
        else:
            print("Acceso denegado, eres externo y no has entrado entre las 10 y 18.")
    
    

            