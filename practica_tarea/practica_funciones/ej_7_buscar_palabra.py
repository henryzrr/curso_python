# ok
n = int(input("Cuantas palabras desea ingresar? :"))
ls = [input() for i in range(n)]

palabra=input("Ingrese la palabra que desea buscar: ")
ls_res =[]
for cad in ls:
    if palabra.upper() in cad.upper():
        ls_res.append(cad)

print("\nLas coincidencias encontradas para '%s' con un for normal es:"%(palabra))
print("res=",ls_res)

print("\nLas coincidencias encontradas para '%s' con listas de comprension es:"%(palabra))
ls_res2 = [cad for cad in ls if palabra.upper() in cad.upper()]
print("res=",ls_res2)

