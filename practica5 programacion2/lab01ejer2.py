import math

class Estadisticas:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        return sum(self.datos) / len(self.datos)

    def desviacion(self):
        media = self.promedio()
        suma_cuadrados = sum((x - media) ** 2 for x in self.datos)
        return math.sqrt(suma_cuadrados / (len(self.datos) - 1))
numeros = []
for i in range(10):
    num = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)
estadisticas = Estadisticas(numeros)
prom = estadisticas.promedio()
desv = estadisticas.desviacion()
print(f"\nEl promedio de los números es: {prom:.4f}")
print(f"La desviación estándar es: {desv:.4f}")