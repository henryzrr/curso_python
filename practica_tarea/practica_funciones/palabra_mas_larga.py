palabra1 = input("Ingrese palabra1:\n")
palabra2= input("Ingrese palabra2:\n")

def get_diferencia():
    tam1 = len(palabra1)
    tam2 = len(palabra2)

    tam_dif = 0
    if tam1>tam2:
        tam_dif = tam1-tam2  
    else:
        palabra1,palabra2 = palabra2,palabra1
        tam_dif = tam2-tam1
    print(palabra1)
    print("La palabra %s tiene %i mas que %s." % (palabra1,tam_dif,palabra2))