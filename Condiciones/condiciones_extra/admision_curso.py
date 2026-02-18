"""
Ejercicio 3 

Admisión a un curso.
Un centro formativo decide quién puede entrar a un curso según la edad, la nota de una prueba, el
nivel previo y las plazas disponibles.
El programa debe pedir:
- edad,
- nota de la prueba (0–100),
- nivel previo (ninguno / básico / intermedio),
- y cuántas plazas quedan.
Reglas:
- si no quedan plazas, se rechaza directamente;
- si la edad es menor de 16, también se rechaza;
- si el nivel es “ninguno”, la nota mínima es 70;
- si el nivel es “básico”, la nota mínima es 55;
- si el nivel es “intermedio”, la nota mínima es 40;
- si la edad es 30 o más, la nota mínima baja 5 puntos (pero nunca puede bajar de 35).
El programa debe decir admitido/rechazado e indicar la nota mínima que se ha usado y por qué 

"""

edad = int(input("Introduce tu edad: "))
nota = int(input("Introduce tu nota de la prueba: "))
nivel = input("Introduce tu nivel previo (ninguno / básico / intermedio): ").lower()
plazas = int(input("Introduce cuantas plazas quedan: "))

nota_minima = 0

if plazas == 0:
    print("\nRECHAZADO\n\nPorque no quedan las plazas. ")
    exit()

if edad < 16:
    print("\nRECHAZADO\n\nPorque eres menor de 16.")
    exit()

else:    
    if nivel == "ninguno":
        nota_minima = 70
        print(f"Se aplica la nota minima a {nota_minima}, porque tu nivel es {nivel}.")
                
    elif nivel == "basico" or nivel == "básico":
        nota_minima = 55
        print(f"Se aplica la nota minima a {nota_minima}, porque tu nivel es {nivel}.")

    elif nivel == "intermedio":
        nota_minima = 40
        print(f"Se aplica la nota minima a {nota_minima}, porque tu nivel es {nivel}.")

    else:
        print("Nivel no valido.")
        exit()

    if edad >= 30:
        nota_minima -= 5
        print(f"Se baja 5 puntos a la nota minima, porque tu edad es de 30 o más.")

        if nota_minima <35:
            nota_minima = 35
            print("Tu nota minima se queda en 35 puntos, porque no puede bajar mas de 35.")

    if nota >= nota_minima:
        print(f"\nADMITIDO\n\nLa nota minima usada es de: {nota_minima}.\nTu nota es de: {nota}.")
    else:
        print(f"\nRECHAZADO\n\nLa nota minima usada es de: {nota_minima}.\nTu nota es de: {nota}.") 