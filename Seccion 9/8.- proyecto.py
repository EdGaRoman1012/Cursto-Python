import os
import re
import time
from datetime import datetime

def buscar_numeros_serie(directorio_raiz):
    patron = re.compile(r'[N][a-zA-Z]{3}-\d{5}')
    resultados = []

    # Obtener la fecha de hoy en formato dd/mm/aa
    fecha_hoy = datetime.now().strftime('%d/%m/%y')

    # Iniciar el tiempo de búsqueda
    inicio_tiempo = time.time()

    for directorio_actual, carpetas, archivos in os.walk(directorio_raiz):
        for nombre_archivo in archivos:
            ruta_completa = os.path.join(directorio_actual, nombre_archivo)

            with open(ruta_completa, 'r') as archivo:
                contenido = archivo.read()
                coincidencias = patron.findall(contenido)

                for coincidencia in coincidencias:
                    resultados.append((nombre_archivo, coincidencia))

    # Calcular la duración de la búsqueda
    duracion_busqueda = round(time.time() - inicio_tiempo)

    # Presentar los resultados en formato de tabla
    print("----------------------------------------------------")
    print(f"Fecha de búsqueda: {fecha_hoy}\n")
    print("ARCHIVO\t\tNRO. SERIE")
    print("-------\t\t----------")

    for resultado in resultados:
        print(f"{resultado[0]}\t{resultado[1]}")

    print(f"\nNúmeros encontrados: {len(resultados)}")
    print(f"Duración de la búsqueda: {duracion_busqueda} segundos")
    print("----------------------------------------------------")

# Reemplaza 'ruta/del/directorio' con la ruta real a la carpeta que has descomprimido.
directorio_raiz = 'C:\\Users\\XMX8224\\Documents\\Curso Python\\Seccion 9\\proyecto\\Mi_Gran_Directorio'
buscar_numeros_serie(directorio_raiz)

