"""Escribe un programa que solicite al usuario su nombre y edad, y luego muestre un mensaje con esa
información en el formato:"Hola, [nombre]. Tienes [edad] años."""

nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))

print(f"Hola,{nombre}.Tienes {edad} años")