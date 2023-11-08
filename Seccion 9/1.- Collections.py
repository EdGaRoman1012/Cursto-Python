from collections import Counter,defaultdict,namedtuple
numero = [1,2,3,4,5,4,2,3,1,5,6,7,8,3,2,3]

print(Counter(numero))

mi_dic = defaultdict(lambda : 'nada')

mi_dic['uno'] = 'verde'

print(mi_dic['uno'])

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona("ariel",1.34,59)
print(ariel.nombre)



