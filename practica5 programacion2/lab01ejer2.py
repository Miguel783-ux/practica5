class Matriz:
    def _init_(self, datos):
        self.datos = datos
        self.filas = len(datos)
        self.columnas = len(datos[0]) if self.filas > 0 else 0
    def _add_(self, otra):
        if self.filas != otra.filas or self.columnas != otra.columnas:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumarse.")
        resultado = [
            [self.datos[i][j] + otra.datos[i][j] for j in range(self.columnas)]
            for i in range(self.filas)
        ]
        return Matriz(resultado)
    def _str_(self):
        return '\n'.join([' '.join(map(str, fila)) for fila in self.datos])
m1 = Matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matriz([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
resultado = m1 + m2
print("Matriz 1:")
print(m1)
print("\nMatriz 2:")
print(m2)
print("\nSuma de las matrices:")
print(resultado)