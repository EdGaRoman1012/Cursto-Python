class Pajaro:
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"Pio, Mi color es {self.color}")

    def volar(self, metros):
        print(f"El pajaro a volago {metros} metros")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")

    @staticmethod
    def mirar():
        print("El pajaro mira")

Pajaro.poner_huevos(3)
Pajaro.mirar()