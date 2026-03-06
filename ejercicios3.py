#Resolver la ecuacion cuadratica 2X**2-7X+3=0
a=int(input("Ingrese el valor a:"))
b=int(input("Ingrese el valor b:"))
c=int(input("Ingrese el valor c:"))
x1=-b+((b**2-4*a*c)**0.5)/(2*a)
x2=-b-((b**2-4*a*c)**0.5)/(2*a)
print("el resutado de la primera ecuacion es:",x1,"y de la segunda ecuacion es:" ,x2) 