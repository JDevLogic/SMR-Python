"""
Ejercicio 15 

Riesgo de fraude en una compra.
Una tienda online marca el riesgo de una compra.

El programa debe pedir:
- importe,
- país (ES / UE / fueraUE),
- método (tarjeta / paypal / transferencia),
- y si el cliente es nuevo (sí/no).

Reglas:
- fueraUE + tarjeta + importe > 300 → riesgo ALTO;
- cliente nuevo e importe > 200 → riesgo MEDIO (si no era ALTO);
- transferencia es BAJO, salvo si el importe > 1000, que pasa a MEDIO;
- paypal en UE → BAJO;
- en ES el riesgo es BAJO, salvo si el importe > 800, que pasa a MEDIO.

Muestra BAJO/MEDIO/ALTO y explica qué regla se ha aplicado. 

"""

