"""
Ejercicio 2 — Compra online con factores variables (2.5)

Una tienda online quiere comprobar si una compra puede realizarse y cuál será su precio final. Para ello
necesita tener en cuenta el tipo de cliente, posibles descuentos, el método de pago y algunas condiciones
especiales que pueden ocurrir dependiendo del día o del tipo de envío.

El programa debe pedir al usuario:
- importe de la compra
- tipo de cliente (normal, premium, empresa)
- método de pago (tarjeta, paypal, transferencia)
- si tiene cupón de descuento (si / no)

Además, el sistema genera automáticamente algunas condiciones del día:
- día promocional: elegir un número aleatorio entre 1 y 7
- envío express: elegir aleatoriamente entre 0 y 1

Reglas del sistema:
- si el importe es menor o igual que 0 → Importe no válido

- descuentos base:
• normal → 0%
• premium → 10%
• empresa → 15% solo si el importe es ≥ 200

- si hay cupón → se aplica un 5% extra, pero no se combina con el descuento de empresa
- si el día promocional es 6 o 7 y el cliente es premium → se añade otro 5% de descuento
- si envío express = 1 → se añaden 12 € al precio; si el total supera 100 €, ese recargo pasa a ser de 5 €

- restricciones de pago:
• paypal no permitido si el total supera 300 €
• transferencia no permitida si el total es menor de 20 €

El programa debe mostrar:
- si la compra es válida o no
- el precio final
- qué descuentos o recargos se han aplicado (o el motivo del rechazo) 

"""
import random

importe = float(input("Introduce el importe de la compra: "))
tipo_cliente = input("Introduce que tipo de cliente eres (normal, premium, empresa): ").strip().lower()
metodo_pago = input("Introduce el metodo de pago (tarjeta, paypal, transferencia): ").strip().lower()
cupon_descuento = input("Introduce si tienes cupon de descuento o no (si / no): ").strip().lower().replace("í","i")

dia_promocional = random.randint(1,7)
envio_express = random.randint(0,1)

if importe <= 0:
    print("Importe no valido.")

else:
    descuento = 0
    
    if tipo_cliente == "premium":
        descuento = 10
        print("Tu descuento es del 10% porque eres premium.")
    elif tipo_cliente == "empresa" and importe >= 200:
        descuento = 15
        print("Tu descuento es del 15% porque eres empresa y tu importe es mayor o igual a 200.")
    
    if cupon_descuento == "si" and not(tipo_cliente == "empresa" and importe >= 200):
        descuento += 5
        print("Se aplica un 5% extra")

    if (dia_promocional == 6 or dia_promocional == 7) and tipo_cliente == "premium":
        descuento += 5
        ("Se aplica un 5% extra porque es dia promocional es 6 o 7 y eres premium.")
    
    total = importe *(descuento/100)

    if envio_express == 1:
        recargo = 12
        print("Hay envio express, se añaden 12 € al precio.")
    
    if total + recargo > 100:
        recargo = 5
        total += recargo
        print("El recargo es de 5 porque supero los 100")
    
    if metodo == "paypal" and total > 300:
        print("Compra no permitida porque Paypal no permite si el total supera 300€")
    elif metodo == "tranferencia" and total < 20:
        print("Compra no permitida porque es transferencia y el total es menor de 20€.") 

    else:
        print("Compra valida.")
        print(f"{total:.2f}")   
