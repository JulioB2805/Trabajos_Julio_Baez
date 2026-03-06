#Dados dos números leídos por teclado, imprimir el mayor y si es par o impar
N1=int(input("Ingrese un valor= "))
N2=int(input("Ingrese otro valor= "))
if N1>N2:
        print("El mayor es: ",N1)
elif N1<N2:
        print("El mayor es: ",N2)
else:
        print("Son numeros iguales.")  
if N1 % 2== 0:
    print("Es un numero par.")
else:
     print("Es un numero impar.")
