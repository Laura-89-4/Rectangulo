# Programa que modela un rectángulo y calcula su perímetro

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


print("== Cálcular el perímetro de un rectángulo ==")
print("Ingrese la base del rectangulo")
base = float(input())
print("Ingrese la altura del rectangulo")
altura = float(input())

mi_rectangulo = Rectangulo(base, altura)

print("Base:", mi_rectangulo.base)
print("Altura:", mi_rectangulo.altura)
print("El perímetro del rectángulo es:", mi_rectangulo.perimetro())


    
