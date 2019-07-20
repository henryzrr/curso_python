# ok
a={'Jose':18}
b={'Maria':15}
c={'Pedro': 24}
ascendente=True
a.update(b)
a.update(c)
print("3 diccionarios ordenados descendentemente:")
ls=sorted(a, key = lambda x: a[x],reverse=True)
cad=""
for i in ls:
    cad+=("'%s':%i "%(i,a[i]))
print("("+cad+")")
print("3 diccionarios ordenados ascendentemente:")
ls=sorted(a, key = lambda x: a[x],reverse=False)
cad=""
for i in ls:
    cad+=("'%s':%i "%(i,a[i]))
print("("+cad+")")
