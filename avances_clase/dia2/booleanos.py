import random
num_al = [random.randint(1,100) for i in range(200)]
for i in range(1,198):
    if (num_al[i]<num_al[i+1]<num_al[i+2]) and not (num_al[i]&1) and not(num_al[i+1]&1) and not (num_al[i+2]&1):
        print("se encontraron 3 numeros ordenados de mayor a menor y que ademas son pares")
        print("{}, {}, {}".format(num_al[i],num_al[i+1],num_al[i+2]))
        
print("")

lis_bool = [random.randint(0,2) for i in range(2)]
bool_res = False
for i in lis_bool:
    bool_res = bool_res or bool(i)

print("El valor boleano aleatorio aplicando una operacion or sobre una lista de dos elementos es:")
print(bool_res)
print("")
lsNum = range(1,100)
lsPares=[]
for i in lsNum:
    if not (i&1):
        lsPares.append(i)
                                       
print("Los numero pares del uno al 100 son:")
print(lsPares)

personas = [("juan",13),("raul",1),("pedro",53),("maria",83),("felipe",23),("diana",15)
            ,("juana",19),("tadeo",8),("martha",3),("dennis",130),("carlos",100),("ana",11),
            ("pele",18),("rigoberto",17),("leticia",53),("patricia",53),("fenanda",33),("teresa",15)]

print("\n")
print("Buscando personas de la misma edad\n")
tam = len(personas)
for i in range(tam-1):
    for j in range(i+1,tam):
        if personas[i][1]==personas[j][1]:
            print(personas[i][0]+" "+personas[j][0]+" tienen la misma edad") 
    