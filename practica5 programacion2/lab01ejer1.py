import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return self.b ** 2 - 4 * self.a * self.c

    def getRaiz1(self):
        discriminante = self.getDiscriminante()
        if discriminante >= 0:
            return (-self.b + math.sqrt(discriminante)) / (2 * self.a)
        return None

    def getRaiz2(self):
        discriminante = self.getDiscriminante()
        if discriminante > 0:
            return (-self.b - math.sqrt(discriminante)) / (2 * self.a)
        return None

    def resolver(self):
        discriminante = self.getDiscriminante()
        if discriminante > 0:
            r1 = self.getRaiz1()
            r2 = self.getRaiz2()
            print(f"Las raíces de la ecuación son: r1 = {r1:.4f}, r2 = {r2:.4f}")
        elif discriminante == 0:
            r1 = self.getRaiz1()
            print(f"La ecuación tiene una única raíz: r = {r1:.4f}")
        else:
            print("La ecuación no tiene raíces reales.")
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))
ecuacion = EcuacionCuadratica(a, b, c)
ecuacion.resolver()