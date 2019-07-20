# ok
from random import randint
import time

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

def mayor3(lista):
    return max(lista)
        

ls = [randint(1,1000) for i in range(50)]
print("La lista generada aleatoria usada para buscar el mayor es:\n")
print(ls)
print("\nAplicando la funcion 1 el numero mayor es:")
start = time.time()
print((mayor1(ls))[49], end=' ')
end = time.time()
print('time: ', end -start)

print("\nAplicando la funcion 2 el numero mayor es:")
start = time.time()
print((mayor2(ls[0],ls[1:])), end=' ')
end = time.time()
print('time: ', end -start)

print("\nAplicando la funcion 3 el numero mayor es:")
start = time.time()
print(mayor3(ls), end=' ')
end = time.time()
print('time: ', end -start)


