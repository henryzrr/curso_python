import random

ls_a = [random.randint(0,1001) for i in range(20)]
ls_b = [random.randint(0,1001) for i in range(20)]
print("----------------------------------------")
print("suma de dos listas:\n")
print("lista a {}".format(ls_a))
print("lista b {}".format(ls_b))

for i in range(20):
    ls_a[i] = ls_a[i]+ls_b[i]
print("\nla suma de las listas es:")
print(ls_a)
print("----------------------------------------\n")
print("----------------------------------------")
print("Programa que calcula muestra numeros primos hasta 'N'\n")

print("----------------------------------------")

print("ordenando la lista 'ls_a'")
ls_a.sort()
print(ls_a)