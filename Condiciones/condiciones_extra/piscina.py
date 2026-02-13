"""
Ejericico 1 

Piscina municipal.
En una piscina pública hay varias normas de acceso que dependen de la edad, la hora y del aforo.
El programa debe pedir:
- si la persona entra con bono o con entrada de día,
- su edad,
- la hora a la que quiere entrar (de 0 a 23),
- y el porcentaje de ocupación actual (0 a 100).
Ten en cuenta que:
- cuando el aforo está casi lleno (95% o más), solo pueden entrar personas con bono;
- los menores de 12 años solo pueden entrar entre las 10 y las 19 (incluidas);
- las personas mayores de 65 años tienen descuento, pero solo fuera de las horas punta (de 16 a 20).
El programa debe decir si puede entrar o no y explicar claramente el motivo. Si entra, indica también
qué tarifa le toca (normal / infantil / descuento).

"""

acceso = input("Introduce tu tipo de acceso bono / entrada: ").lower()
edad = int(input("Introduce tu edad: "))
hora = int(input("Introduce tu hora de ingreso: "))
ocupacion = int(input("Introduce la ocupacion actual: "))


if ocupacion >= 95 and acceso != "bono":
    print("NO PUEDES ACCEDER\nPorque no tienes bono y esta casi lleno. ")


elif edad <12 and not(hora >= 10 and hora <=19):
    print("NO PUEDES ACCEDER\nPorque eres menor de 12 y solo pueden entrar entre las 10 y las 19 (incluidas). ")

else:
    print("PUEDES ENTRAR")
    
    if edad < 12:
        print("TARIFA INFANTIL")
    
    elif edad > 65 and (hora < 16 or hora > 20):
        print("TARIFA CON DESCUENTO")
    
    else:
        print("TARIFA NORMAL")






