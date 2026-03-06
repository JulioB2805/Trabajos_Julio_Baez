import time,os,random
def lanzar_dados():
 num1=random.randrange(1,7)
 num2=random.randrange(1,7)
 return(num1,num2)

while True:
 num1=int(input("1. Ingrese el primer numero del dado: "))
 num2=int(input("2. Ingrese segundo numero del dado: "))
 if num1 and num2  >=1 and num1 and num2 <=6:
     os.system("cls")
     print(f"Elegiste los numeros {num1} y {num2}")
     cond=input("¿Esta correcto?(si,no): ")
     if cond== "si":
          print("Estamos girando los dados...")
          time.sleep(1.5)
          dado=lanzar_dados()
          if dado==num1:
              print(f"Ha caido el {dado} acertaste!!")
          else:
              print(f"oh oh, ha caido {dado}intentalo de nuevo.")
     elif cond=="no":
          print("Vuelva a introducir los numeros.")
     else:
        print("Datos incorrectos.")
 else:
  print("¡No corresponde!")
 time.sleep(1.5)
 print("---Juego terminado---")