import zipfile

import  shutil

#mi_zip = zipfile.ZipFile('curso.zip', 'w')
#mi_zip.write('curso.txt')

#mi_zip.close()

#zip_abierto = zipfile.ZipFile('curso.zip', 'r')

#zip_abierto.extractall()

#carpeta_origen = 'C:\\Users\XMX8224\Documents\Curso Python\Seccion 9\curso.txt'

#archivo_destino = 'comprimido'

#shutil.make_archive(archivo_destino, 'zip',carpeta_origen)

shutil.unpack_archive('comprimido.zip', 'Curso', 'zip')
