#Imprimir todos los números pares que existen entre dos números leídos por teclado usando bucles for.
N1=int(input("Ingrese un valor de inicio= "))
N2=int(input("Ingrese otro valor limite= "))
for x in range(N1,N2,2):
   print(x)