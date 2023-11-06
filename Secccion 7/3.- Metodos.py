class Pajaro:
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"Pio, Mi color es {self.color}")

    def volar(self, metros):
        print(f"El pajaro a volago {metros} metros")

piolin = Pajaro("Amarillo", "Ave")
piolin.piar()