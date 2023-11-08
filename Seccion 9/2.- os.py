import os
import shutil
import send2trash
print(os.getcwd())

archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir())

#shutil.move('curso.txt', 'c:\\Users\\XMX8224\\Desktop')

#send2trash.send2trash('curso.txt')

#print(os.walk('C:\\Users\XMX8224\Desktop\MALLAs'))

ruta = 'C:\\Users\\XMX8224\\Desktop\\MALLAs'


