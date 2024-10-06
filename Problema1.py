#Implemente un programa que solicite al usuario una fracción, con
#formato X/Y, donde cada uno de X e Y es un número entero, y luego
#muestra, como un porcentaje redondeado al número entero más
#cercano, donde se indicará la cantidad de combustible en el
#tanque. Se debe tener en cuenta los siguientes casos:
#- Colocar E en caso X/Y sea menor a 1% del total
#- Colocar F en caso X/Y sea mayor a 99%.
#- En otro caso, devolver el valor en porcentaje %
#También debe tomar en cuenta los siguientes casos:
#- X y Y deben ser números enteros
#- X debe ser menor o igual a Y, y Y != 0
#De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
#cualquier excepción como ValueError o ZeroDivisionError
def Fraccion():
    while True:
        try:
            entrada = input("Ingrese una fracción en formato X/Y: ")
            x1,y1=entrada.split('/')
            x2=int(x1)
            y2=int(y1)
            
            div=(x2/y2)*100
            divR= round(div)
            #Si es menor que uno nos devuelve E
            if divR < 1:
                print('E')
            #Si es mayor que uno nos devuelve F
            elif divR>99:
                print('F')
            else:
                return f"{divR}%"
            
        except ValueError:
            print("Error dado que solo se permiten números enteros ValueError")
        except ZeroDivisionError:
            print('Volver a preguntar al usuario dada la excepción ZeroDivisionError')
        else:
            break

if __name__ == '__main__':
    print(Fraccion())