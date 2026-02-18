"""
Ejercicio 8 

Inicio de sesión con bloqueo.
Un sistema guarda cuántos intentos fallidos lleva una cuenta.

El programa debe pedir:
- intentos fallidos previos (0–5),
- usuario,
- contraseña introducida.

Usuario correcto: admin
Contraseña correcta: Python2026

Reglas:
- si los intentos son 5 o más, la cuenta está bloqueada (ni se comprueba nada);
- si el usuario es incorrecto, se suma 1 intento y se muestra “usuario incorrecto”;
- si el usuario es correcto pero la contraseña no, se suma 1 intento y se muestra “contraseña incorrecta”; 
- si todo es correcto, se concede el acceso y los intentos pasan a 0.

Muestra el mensaje y el número de intentos que quedan después.

"""

intentos = int(input("Introduce los intentos fallidos previos: "))
usuario = input("Introduce el usuario: ")
contraseña = input("Introduce la contraseña: ")

user = "admin"
password = "Python2026"

intentos_restantes = 0

if intentos >= 5:
    print("Tu cuenta esta bloqueada, porque el numero de intentos son 5 o mas.")
    exit()


if usuario != user:
    print("\nUsuario incorrecto.")
    intentos =+ 1
    
    
elif contraseña != password:
    print("\nContraseña incorrecto.")
    intentos =+ 1

else:

    print("\nACCESO CONCEDIDO.")
    intentos = 0
    print("Tu intentos se restablecen a 0.")

intentos_restantes = 5 - intentos
    
print(f"Tu numero total de intentos son: {intentos}\n")
print(f"Tu numero de intentos restantes son: {intentos_restantes}\n")    