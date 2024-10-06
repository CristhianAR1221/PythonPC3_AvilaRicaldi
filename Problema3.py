#Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
#“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.
#Cree 2 objetos de tipo circulo y calcule su área.
import math
class CIRCULO:
    
    def __init__ (self,radio)-> None:
        self.radio=radio
        pass
    
    #metodos
    def Area(self):
        area=float(math.pi*self.radio**2)
        return area
    pass

    def Imprimir(self):
        print(f"El area del circulo es: {self.Area()}")


if __name__ == '__main__':
    CIRCULO1=CIRCULO(3)
    CIRCULO2=CIRCULO(10)

    CIRCULO1.Imprimir()
    CIRCULO2.Imprimir()
