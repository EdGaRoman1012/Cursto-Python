# def perdir_numero():
#     while True:
#         try:
#             numero = int(input("Dame un numero: 2"))
#         except:
#             print("Ese no es un numero")
#         else:
#             print(f"Ingresaste el numero {numero}")
#             break
#     print("Gracias")
# perdir_numero()

def suma(num1,num2):
    try:
        resultado = num1+num2
    except:
        print(f"Error inesperado")
    else:
        print(f"La suma es {resultado}")
        


suma(1,2)
