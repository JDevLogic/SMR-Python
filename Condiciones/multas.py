""" 
Ejercicio 8 

Un sistema de multas clasifica la infracción según velocidad. Solicita límite de la vía y
velocidad detectada. - Hasta +10 km/h: sin multa. - +11 a +30 km/h: infracción leve. - +31 a
+50 km/h: infracción grave. - Más de +50 km/h: infracción muy grave. Muestra el tipo de
infracción 

"""

limite = int(input("Introduce el limite de velocidad de la via: "))
velocidad = int(input("Introduce la velocidad detectada: "))

exceso = velocidad - limite

if exceso <= 10:
    print("No tienes multa.")

elif exceso >= 11 and exceso <= 30:
    print("Infraccion leve.")

elif exceso >= 31 and exceso <= 50:
    print("Infraccion grave.")

elif exceso > 50:
    print("Infraccion muy grave.")