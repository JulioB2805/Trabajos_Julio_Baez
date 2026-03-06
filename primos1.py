#Desarrollar un programa que encuentre números primos
numero=1000000
while True:
    numero=numero+1
    es_primo=True
    for x in range(2,int(numero/2)):
        if numero % x == 0:
            es_primo=False
            break
    if es_primo:
                print(numero)