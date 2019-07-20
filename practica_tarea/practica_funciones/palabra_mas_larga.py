# ok
palabra1 = input("Ingrese palabra1: ")
palabra2 = input("Ingrese palabra2: ")

def get_diferencia(palabra1,palabra2):
    tam_dif = len(palabra1) - len(palabra2)
    if tam_dif < 0 :
        palabra1, palabra2 = palabra2, palabra1
        tam_dif *=-1
    print("La palabra %s tiene %i letras mas que %s." % (palabra1,tam_dif,palabra2))

get_diferencia(palabra1,palabra2)
