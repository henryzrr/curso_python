# ok
num1 = int(input("Ingrese num 1: "))
num2 = int(input("Ingrese num 2: "))

if num2!=num1:
    if num1>num2:
        num1,num2=num2,num1
    print("La suma entre %i y %i es:" % (num1,num2))
    print(sum(range(num1+1,num2)))
else:
    print("No se ingreso un rango valido")
