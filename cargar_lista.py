lista=[]
def cargar_lista():
    v=input("Ingrese un valor: ")
    lista.append(v)
def imprimir_lista():
        print("Elementos de la lista")
        print(lista)
while True:
    print("Gestionar lista")
    opcion=int(input("1.cargar\n2.Imprimir\n0.Salir\nElige: "))
    if (opcion==1):
        cargar_lista()
    elif(opcion==2):
         imprimir_lista()
    elif(opcion==0):
         print("Error")
         break
    else:
        print("No entiendo esa orden.") 