from functools import reduce

def invertir1(n):
    ls = list(n)
    ls.reverse()
    return "".join(ls)

def invertir2(n):
    cad_fin=""
    for i in n:
        cad_fin = i+cad_fin
    return cad_fin

def invertir_recursivo(n,i,tam):
    return (invertir_recursivo(n,i+1,tam)+n[i] if i<tam else "")

def verificar(boolean,n):
    return True and boolean if ord(n)>=48 and ord(n)<=57 else False

def es_numero(n):
    return reduce(verificar,n)    

def get_numero():
    numero = input("\nIngrese el numero que desea invertir, puede ser de cualquier tamaño:\n")
    return numero

def invertir_como_num(n):
    ni = 0
    while n>0:
        aux = n%10
        ni = (ni*10)+aux
        n=n//10
    return ni

def invertir_como_num_recursivo(n):
    if n>0:
        return (invertir_como_num_recursivo(n/10)*10)+n%10
    else:
        return 1

def invertir_numero():
    num = get_numero()
    while not es_numero(num):
        print("Usted no ingreso un numero valido")
        num = get_numero()
    print("----- NUMERO TRATADO COMO CADENA ----\n")
    print("\nEl numero invertido con la funcion 1 es:")
    print(invertir1(num))
    print("\nEl numero invertido con la funcion 2 es:")
    print(invertir2(num))
    print("\nEl numero invertido con la funcion 3 (recursiva) es:")
    print(invertir_recursivo(num,0,len(num)))
    print("\n-------- NUMERO TRATADO COMO NUMERO -----\n")
    num = int(num)
    print("\nEl numero invertido con la funcion 4 es:")
    print(invertir_como_num(num))
    print("\nEl numero invertido con la funcion 5 (recursiva) es:")
    print(invertir_como_num(num))


invertir_numero()