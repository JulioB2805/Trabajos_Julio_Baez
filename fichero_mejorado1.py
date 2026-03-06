# escritura
fichero=open('data.txt','w')
texto= input("Ingrese su texto a guardar: ")
fichero.write(texto)
fichero.close()

# append, actualizar fichero
fichero = open('data.txt', 'a')

texto=input("Agregue otro texto: ")
fichero.write(f"\t{texto}")
fichero.close()

# leer fichero
fichero= open('data.txt', 'r')
for x in fichero:
    print(x)
fichero.close()