palabra1 = input("Ingrese palabra1: ")
palabra2 = input("Ingrese palabra2: ")

def get_diferencia(palabra1,palabra2):
    tam1 = len(palabra1)
    tam2 = len(palabra2)

    tam_dif = 0
    if tam1>tam2:
        tam_dif = tam1-tam2  
    else:
        palabra1,palabra2=palabra2,palabra1
        tam_dif = tam2-tam1
    print("La palabra %s tiene %i letras mas que %s." % (palabra1,tam_dif,palabra2))

get_diferencia(palabra1,palabra2)