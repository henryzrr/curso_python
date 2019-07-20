#ok
import functools
from random import randint
def promedio1(ls):
    return sum(ls)/len(ls)

def promedio2(ls):
    sum=0
    tam=0
    for i in ls:
        sum+=i
        tam+=1
    return sum/tam

promedio3 = lambda x : sum(x)/len(x)

suma = lambda x,y:x+y
fun_aux = lambda x : int(x/x)
sum_ls = lambda fun,x: functools.reduce(fun,x)
get_tam = lambda fun,x: sum(list(map(fun,x)))
promedio4 = lambda x:sum_ls(suma,x)/get_tam(fun_aux,x)


ls = [randint(1,100) for i in range(50)]

print("Lista de 50 numeros aleatorios del  1 al 100")
print(ls)
print("\nEl promedio con la funcion 1 es:")
print(promedio1(ls))
print("\nEl promedio con la funcion 2 es:")
print(promedio2(ls))
print("\nEl promedio con la funcion 3 es:")
print(promedio3(ls))
print("\nEl promedio con la funcion 4 es:")
print(promedio4(ls))


