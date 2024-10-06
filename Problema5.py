#Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos
#para:
#1. Display - Debe mostrar toda la información del estudiante (nombre y número de
#registro).
#2. setAge - Debe asignar la edad al estudiante
#3. setNota - Debe asignar las notas al estudiante.
class Alumno:
    def __init__(self, nombre, n_registro):
        self.nombre = nombre
        self.n_registro = n_registro
        
    def Display(self):
        print(f'Nombre: {self.nombre}, N° Registro: {self.n_registro}')


    def setAge(self, edad):
        print(f'La edad del estudiante {self.nombre} (N° Registro: {self.n_registro}) se ha establecido en: {edad}')


    def setNota(self, nota):
        print(f'La nota {nota} se ha asignado al estudiante {self.nombre} (N° Registro: {self.n_registro})')


if __name__ == '__main__':
    alumno1 = Alumno("Diego Benites", "1111222")
    alumno1.Display()
    alumno1.setAge(20)  
    alumno1.setNota(15)
