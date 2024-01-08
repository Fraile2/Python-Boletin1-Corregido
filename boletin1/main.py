from random import randint

divisores=[]
no_salir=True

while no_salir:
    divisores.clear()
    aleatorio=randint(10000000, 50000000)
    
    if aleatorio%2==0:
        divisores.append(aleatorio//2)
    else:
        for n in range(2, aleatorio//2):
            if aleatorio%n==0:
                divisores.append(n)
        if not divisores:
            no_salir=False

print(f"El numero {aleatorio} es primo.")