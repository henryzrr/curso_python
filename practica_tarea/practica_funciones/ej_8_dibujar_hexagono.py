lado = int(input("Ingrese tamaño: "))
ciclo = (lado*2)-1
espacio=lado-1
ladoaux=lado
for i in range(lado):
    cad=espacio*" "+ladoaux*"*"+espacio*" "
    espacio =espacio-1
    ladoaux = ladoaux+2
    print (cad)
espacio=espacio+2
ladoaux = ladoaux-4
lado -=1
for i in range(lado):
    cad=espacio*" "+ladoaux*"*"+espacio*" "
    espacio =espacio+1
    ladoaux-=2
    print (cad)

