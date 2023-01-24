
class OperasBas:
    # propiedades de clase
    n1 = 0
    n2 = 0
    res = 0
    # constructor de clase
    def __init__(self):  # sefl es el this de JAVA pero en Python
        pass
    # Metodos de clase

    def suma(self):
        self.res = self.n1+self.n2
    def resta(self):
        self.res = self.n1-self.n2

def main():
    obj=OperasBas(3,2)
    obj.suma()

if __name__ == '__main__':
    main()
