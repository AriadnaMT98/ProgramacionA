class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.141592 * self.radio * self.radio

    def calcular_perimetro(self):
        return 2 * 3.141592 * self.radio