import datetime

#mi_hora = datetime.time(17, 35)
#mi_fecha = datetime.date(2229 , 12, 30)
#print(mi_fecha.ctime(), mi_fecha.today())

#otra_fecha = datetime(2025,5,14,22,10,12,213)

#print(otra_fecha.replace(month=10))

#nacimiento = datetime(1992,3,2, 12,23,22)
#defuncion = datetime(2069,12,2,15,12,23)

#vida = defuncion - nacimiento
#print(vida)

hora_actual = datetime.datetime.now().minute

print(hora_actual)