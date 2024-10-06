#Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
#la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
#calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
#cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
#formato. (Los métodos de cadena le serán de utilidad)
def Calificaciones():
    while True:
        try:
            cal = input("Ingrese una lista de calificaciones separadas por comas: ")

            cal_lista = cal.split(',')

   
            calificaciones = [int(calificacion.strip()) for calificacion in cal_lista]

            return calificaciones

        except ValueError:
            
            print("Error: Hay algunas calificaciones no validas")

if __name__ == '__main__':
    calificaciones = Calificaciones()
    print(f"Lista de calificaciones: {calificaciones}")