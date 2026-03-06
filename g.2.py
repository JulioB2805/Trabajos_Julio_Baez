import math

def triangulo():
   lado1 = float(input("Ingrese el primer lado del triángulo: "))
   lado2 = float(input("Ingrese el segundo lado del triángulo: "))
   lado3 = float(input("Ingrese el tercer lado del triángulo: "))
   altura= float(input("Ingrese la altura:"))
   perimetro=lado1+lado2+lado3
   area=(lado1 * altura)/2

   print("el perimetro es:{perimetro}")
   print("el area es:{area}")

def circulo():
   radio=float(input("introduzca su radio:"))

   area = math.pi * radio ** 2
   perimetro = 2 * math.pi * radio
   
   print("el perimetro es: ",perimetro)
   print("el area es: ",area)

def rectangulo():
   lado=float(input("ingrese el valor del lado:"))
   ancho=float(input("Ingrese el valor del ancho:"))

   perimetro=2*lado+2*ancho
   area=lado * ancho
   print("el perimetro es: ",perimetro)
   print("el area es: ",area)

while True:
   print("Menu")
   print(" 1. triangulo")
   print(" 2. Circulo")
   print(" 3. rectangulo")
   print(" 4. salir")

   opcion=input("ingrese un numero")

   if opcion==1:
       triangulo()
   elif opcion==2:
      circulo()
   elif opcion==3:
    rectangulo()

   else:
    break
