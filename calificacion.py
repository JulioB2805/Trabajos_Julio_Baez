#Escriba un programa que recibe las calificaciones de los alumnos de
#la materia de Programación Python e imprime el promedio general.
#El programa se detiene cuando lee el número cero. Tenga en cuenta
#que se desconoce cuantas calificaciones serán introducidas.

suma=0
contador=0

nota=int(input("Ingrese su nota(0 para finalizar): "))

while nota !=0:
    suma=suma+ nota
    contador =contador+1
    nota=int(input("Ingrese su nota(0 para finalizar): "))
if contador > 0:
    promedio=suma/contador
    print(promedio)
else:
    print("Error")