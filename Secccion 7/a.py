class Vertebrado:
    vertebrado = True
# print(Vertebrado.vertebrado)

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

# print(Ave.tiene_pico)
# mi_ave = Ave()
# mi_ave.poner_huevos()

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Pez, Reptil, Ave, Mamifero, Vertebrado):
    pass

mi_mamifero = Ornitorrinco()
mi_mamifero.poner_huevos()
mi_mamifero.tiene_pico
mi_mamifero.vertebrado
mi_mamifero.venenoso
mi_mamifero.nadar()
mi_mamifero.caminar()
mi_mamifero.amamantar()
# Ornitorrinco.venenoso
# Ornitorrinco.nadar()
# Ornitorrinco.caminar()
# Ornitorrinco.amamantar()

