from circulo import Circulo

circulo_uno = Circulo(2)
circulo_dos = Circulo(5)
circulo_tres = Circulo(10)

for circulo in [circulo_uno, circulo_dos, circulo_tres]:
    print("Radio:", circulo.radio)
    print("Área:", circulo.calcular_area())
    print("Perímetro:", circulo.calcular_perimetro())
    print("\n")