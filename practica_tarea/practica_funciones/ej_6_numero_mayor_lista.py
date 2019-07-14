from random import randint

def mayor1(ls):
    ls.sort()
    return ls

def mayor2(n,ls):
    if len(ls)==0:
        return n
    elif len(ls)==1:
        return (ls[0] if ls[0]>n else n)
    else:
        return mayor2((ls[0] if ls[0]>n else n),ls[1:])
        

ls = [randint(1,1000) for i in range(50)]
print("La lista generada aleatoria usada para buscar el mayor es:\n")
print(ls)
print("\nAplicando la funcion 1 el numero mayor es:")
print((mayor1(ls))[49])
print("\nAplicando la funcion 2 el numero mayor es:")
print((mayor2(ls[0],ls[1:])))


