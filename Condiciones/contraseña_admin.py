""" 
Ejercicio 2 

Un sistema de acceso solicita usuario y contraseña. El usuario correcto es 'admin'. La
contraseña debe cumplir: mínimo 8 caracteres, al menos una mayúscula y un número. - Si el
usuario no es correcto, se deniega el acceso. - Si la contraseña no cumple las condiciones, se
muestra el motivo. - Si todo es correcto, se concede el acceso. 

"""

usuario = input("Introduce el nombre de usuario: ")
contraseña = input("Introduce la contraseña: ")

root = "admin"
numero_letras = len(contraseña)
es_mayus = False
hay_digit = False

if usuario == root:
    if numero_letras >= 8:
        for letra in contraseña:
            if letra.isupper() :
                es_mayus = True

            if letra.isdigit():
                hay_digit = True


            
        

elif usuario != root:
    print("El usuario es incorrecto. ")


