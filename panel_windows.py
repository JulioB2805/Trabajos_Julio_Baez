import os
import time

def esperar(texto):
    for x in range(6):
        os.system("cls")
        print(f"Cargando {texto}: {x * 20  } %")
        time.sleep(0.8)
while True:
    os.system("cls")
    print("---Dashboard de windows---")
    op=input("1. Calc\n2. Paint\n3. Apagar\n4. No apagar\n0. Salir\nElija su opcion: ")
    if op=="1":
        esperar ("Calculadora")
        os.system("calc")
    elif op=="2":
        esperar("Paint")
        os.system("mspaint")
    elif op=="3":
        esperar("Apagando en 5 minutos")
        os.system("shutdown -s -t 300")
    elif op==4:
        esperar("cancelar apagado")
        os.system("shutdown -a")
    else:
        print("error")