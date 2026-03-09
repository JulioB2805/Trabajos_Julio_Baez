"""
 cargar una oracion por teclado
 imprime la cantidad de vocales que tiene 
"""
vocales = 0
oracion = input("Ingrese una oracion: ")
longitud = len(oracion)

for i in range(longitud):
    if oracion[i].lower() in "aeiou":
        vocales += 1

print("Su texto ingresado es: ",oracion)
print("La cantidad de vocales es:", vocales)
