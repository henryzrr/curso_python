#busqueda de patrones fuerza bruta
patron = "aba"
cadena = "aboababababaojojobababoojabaojoaba"

tampatron = len(patron)
tamcad = len(cadena)
j=0
posiciones =[]
i=0
while i<tamcad:
    if j==tampatron:
        i =i-tampatron
        posiciones.append(i)
        j=0
    elif cadena[i]==patron[j]:
        j =j+1
    else:
        j=0
    i =i+1
if j==tampatron:
    posiciones.append(i-tampatron)
print("se encontro ocurrencias de '{}' en las posiciones:".format(patron))
print(posiciones)
print("")
print("Cadena original:")

ls_ab = "ab"*20
print (ls_ab)
print("Cadena cortada:")
nueva_lista = ls_ab[0:40:2]
print(nueva_lista)

