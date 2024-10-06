#Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
#ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
#atributos de la clase. Además cree una clase CUADRADO que heredé de rectangulo. Cree un
#objeto de tipo rectangulo y 1 de tipo cuadrado.
class RECTANGULO:
    def __init__ (self,largo,ancho)-> None:
        self.largo=largo
        self.ancho=ancho
        pass
    
    #Metodos 
    def Area(self):
        area=float(self.largo*self.ancho)
        return area
    pass

    def Imprimir(self):
        print(f"El area del rectangulo es: {self.Area()}")


class CUADRADO(RECTANGULO):
    def __init__ (self,largo):
        #Llamamos al constructor  de la clase padre
        super().__init__(largo,largo)
       
    #metodos para imprimi el area del cuadrado
    def Imprimir(self):
        print(f"El área del cuadrado es: {self.Area()}")

        
if __name__ == '__main__':
    RECTANGULO1=RECTANGULO(2,3)
    RECTANGULO2=RECTANGULO(4,5)
    cuadrado1=CUADRADO(6)
    cuadrado2=CUADRADO(7)
    #Imprimmos las areas de los circulos

    RECTANGULO1.Imprimir()
    RECTANGULO2.Imprimir()  
    cuadrado1.Imprimir()
    cuadrado2.Imprimir()