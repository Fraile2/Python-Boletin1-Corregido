divisores=[]
no_salir=True

while no_salir:
    try:
        numero=int(input("Introduce un numero: "))
        no_salir=False
        for n in range(2, numero//2):
            if numero%n==0:
                divisores.append(n)
        if divisores:
            print(f"{numero} no es primo")
        else:
            print(f"{numero} es primo.")
    except Exception:
        print("No has introducido un numero.")
