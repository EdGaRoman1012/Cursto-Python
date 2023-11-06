# class Vaca:
#     def __init__(self, nombre):
#         self.nombre = nombre 
    
#     def hablar(self):
#         print(self.nombre +" dice muuuuu")

# class Oveja:
#     def __init__(self, nombre):
#         self.nombre = nombre 
    
#     def hablar(self):
#         print(self.nombre +" dice beeee")

# vaca1 = Vaca("Auroroa")
# oveja1 = Vaca("Nube")

# class Mago():
#     def atacar(self):
#         print("Ataque mágico")

# class Arquero():
#     def atacar(self):
#         print("Lanzamiento de flecha")

# class Samurai():
#     def atacar(self):
#         print("Ataque con katana")
        

# mi_mago = Mago()
# mi_arquero = Arquero()
# mi_samurai = Samurai()
    
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

mi_mago = Mago()
mi_arquero = Arquero()
mi_samurai = Samurai()


def personaje_defender(objeto):
    objeto.defender()

personaje_defender(mi_mago)


    