import re

text = "Si necesitas ayuda marca al 723-232-2333"

palabra = r'\d{3}-\d{3}-\d{4}'
palabra = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

busqueda = re.search(palabra, text)

#print(busqueda, busqueda.group(1))

#clave = input("Clave: ")

patron = r'\D{1}\w{7}'

#chequear =re.search(patron, clave)
#print(chequear)


def verificar_saludo(frase):
    patron = 'Hola'

    busqueda = re.search(patron, frase)
    if busqueda is None:
        print("No has saludado")
    else:
        print("Ok")
verificar_saludo('Hola, Como estas')


def verificar_cp(cp):
    patron = r'[a-zA-Z]{2}\d{4}'

    busqueda = re.search(patron, cp)

    print(busqueda)

verificar_cp('XX2323')
