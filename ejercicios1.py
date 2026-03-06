print("¡¡Bienvenido al curso!!")
nombre= input("Ingrese su nombre:")
print("Hola",nombre,"!!")
dividendo= int(input("Ingrese el dividendo:"))
divisor= int(input("Ingrese el divisor:"))

if divisor !=0:
    res=dividendo/divisor
else:
    res="Division por cero-indeterminado"
print("El resultado es:" + str(res))