class calculadora:
    num1=None
    num2= None
    resultado=None
    historial=[]

    def __init__(self):
        self.num1=0
        self.num2=0
        self.resultado=0
        self.historial.append("iniciando..")

    def cargar(self, x,y):
        self.num1=x
        self.num2=y
    def sumar(self):
        resultado=self.num1+self.num2
        return resultado
if __name__=="__main__":
    casio=calculadora()
    casio.cargar(12,3)

    print(f"La suma de{casio.num1}y{casio.num2}es {casio.sumar()}")
