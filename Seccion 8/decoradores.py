def decorar_saludos(funcion):

    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("mundo")
    return otra_funcion


@decorar_saludos
def mayuscula(texto):
    print(texto.upper())

@decorar_saludos
def minuscula(texto):
    print(texto.lower())


minuscula("Edgar")