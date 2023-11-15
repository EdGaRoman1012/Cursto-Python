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

age = int(input("Edad: "))
ing= int(input("Ingresos Mensuales: "))

if age >= 16 and ing >= 1000:
    print("Tienes que atributar")
else:
    print("No tienes que atributar")