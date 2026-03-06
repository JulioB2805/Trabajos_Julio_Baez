limite=int(input("Ingrese el valor limite: "))#ingrese su numero limite

for numero in range (2,limite + 1):#empieza en el 2,va hasta el limite y suma de a 1
    es_primo = True

    for i in range(2, numero):
        if numero % i== 0: #numero divido x da cero o no
            es_primo=False
            break
     
    if es_primo:
         print(numero)