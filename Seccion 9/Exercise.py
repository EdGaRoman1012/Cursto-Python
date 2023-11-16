#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
#palabra = input("Escribe una palabra: ")
#for i in range(10):
    #print(palabra)

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

#age = int(input("¿Cuántos años tienes? "))
#for i in range(age):
#    print("Has cumplido " + str(i+1) + " años")


#Escribir un programa que pida al usuario un número entero positivo y muestre
#por pantalla todos los números impares desde 1 hasta ese número separados por comas.

#n = int(input("Introduce un número entero positivo: "))
#for i in range(1, n+1, 2):
#    print(i, end=", ")


#Escribir un programa que pida al usuario un número entero
#positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

#n = int(input("Digita un numero entero positivo: "))

#for i in range(n, -1,-1):
#    print(i, end=", ")


#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

#edad = int(input("¿Cual es tu edad? "))

#if edad >= 18:
#    print("Eres mayor de edad")
#else:
#    print("No eres mayor de edad")


#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
#por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

#passw = "XMX8224"

#password = input("Introduce tu contraseña: ")

#if password.upper() == passw.upper():
#    print("Contraseña valida")
#else:
#    print("Contraseña invalida")

#Escribir un programa que pida al usuario dos números y muestre por
#pantalla su división. Si el divisor es cero el programa debe mostrar un error.

#n1 = int(input("Numero1: "))
#n2 = int(input("Numero2: "))

#if n2 == 0:
#    print(f"Error")
#else:
#    print(f"El resultado es: {n1/n2}")


#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

#n = int(input("Escribe un numero: "))

#if n%2 ==0:
#    print("Es par")
#else:
#    print("Es impar")

#Para tributar un determinado impuesto se debe ser mayor de 16 años y
#tener unos ingresos iguales o superiores a 1000 € mensuales.
#Escribir un programa que pregunte al usuario su edad y sus ingresos
#mensuales y muestre por pantalla si el usuario tiene que tributar o no.

#age = int(input("Edad: "))
#ing= int(input("Ingresos Mensuales: "))

#if age >= 16 and ing >= 1000:
#    print("Tienes que atributar")
#else:
#    print("No tienes que atributar")


#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
#El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres
# con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que
# pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

"""def obtener_grupo(nombre, sexo):
    if (sexo == 'M' and nombre < 'M') or (sexo == 'H' and nombre > 'N'):
        return 'Grupo A'
    else:
        return 'Grupo B'

# Solicitar al usuario su nombre y sexo
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M/F): ")

# Convertir el nombre a mayúsculas para hacer la comparación de manera insensible a mayúsculas/minúsculas
nombre = nombre.upper()

# Obtener el grupo correspondiente
grupo = obtener_grupo(nombre, sexo)

# Mostrar el resultado
print(f"Usted pertenece al {grupo}.")"""

#Escribir un programa que pregunte al usuario
#su renta anual y muestre por pantalla el tipo impositivo
#que le corresponde.


"""def renta_anual(valor):
    if renta <= 10000:
        print(f"Tu renta anual es: {renta * 0.05}")
    elif renta > 10000 and renta < 20000:
        print(f"Tu renta anual es: {renta * 0.15}")
    elif renta > 20000 and renta < 35000:
        print(f"Tu renta anual es: {renta * 0.20}")
    elif renta > 35000 and renta < 60000:
        print(f"Tu renta anual es: {renta * 0.30}")
    elif renta > 60000:
        print(f"Tu renta anual es: {renta * 0.45}")

renta = int(input("Escribe la renta: "))

renta_anual(renta)"""

"""
En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
traduciéndose en mejores beneficios. Los puntos que pueden conseguir 
los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
así como la cantidad de dinero que recibirá el usuario.
"""

def puntuacion_user(puntos):
    if puntos == 0.0:
        print(f"Dinero conseguido: {puntos * 2400}")
    elif puntos == 0.4:
        print(f"Dinero conseguido:{puntos * 2400}")
    elif puntos == 0.6:
        print(f"Dinero conseguido: {puntos * 2400}")
    else:
        print("Elige un valor correcto")

print("""
Registra la puntuacion entre los siguientes valores
0.0\t\t\t0.4\t\t\t0.6
""")
puntaje = float(input(":"))

puntuacion_user(puntaje)



