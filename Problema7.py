import math

class Punto:
    def __init__(self, x=0, y=0):
        self.coordenadaX = x
        self.coordenadaY = y

    def __str__(self):
        return f"({self.coordenadaX}, {self.coordenadaY})"

    def mostrar(self):
        print(f"Coordenada: ({self.coordenadaX}, {self.coordenadaY})")

    def cuadrante(self):
        x = self.coordenadaX
        y = self.coordenadaY

        if x == 0 and y == 0:
            return "Está en el origen."
        elif x == 0:
            return "Está sobre el eje Y."
        elif y == 0:
            return "Está sobre el eje X."
        elif x > 0 and y > 0:
            return "Está en el cuadrante I."
        elif x < 0 and y > 0:
            return "Está en el cuadrante II."
        elif x < 0 and y < 0:
            return "Está en el cuadrante III."
        elif x > 0 and y < 0:
            return "Está en el cuadrante IV."

    def vector(self, otro_punto):
        vector_x = otro_punto.coordenadaX - self.coordenadaX
        vector_y = otro_punto.coordenadaY - self.coordenadaY
        return f"Vector resultante: ({vector_x}, {vector_y})"

    def distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.coordenadaX - self.coordenadaX) ** 2 + (otro_punto.coordenadaY - self.coordenadaY) ** 2)
        return f"Distancia: {distancia:.2f}"

class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()) -> None:
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.coordenadaX - self.punto1.coordenadaX)

    def altura(self):
        return abs(self.punto2.coordenadaY - self.punto1.coordenadaY)

    def area(self):
        return self.base() * self.altura()

    def mostrar_area(self):
        print(f"Área del rectángulo: {self.area():.2f}")


p1 = Punto(2, 3)
p2 = Punto(5, 7)


p1.mostrar()
print(p1.cuadrante())


print(p1.vector(p2))
print(p1.distancia(p2))


rect = Rectangulo(p1, p2)
print(f"Base: {rect.base()}")
print(f"Altura: {rect.altura()}")
rect.mostrar_area()