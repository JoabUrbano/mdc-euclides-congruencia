#Feito por Joab Urbano
import time

class Calcular:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def congruencia(self):
        resto = self.num1%self.num2
        print("{} é congruente a {}(mod {})".format(self.num1, resto, self.num2))

    def mdc_euclides(self):
        var1 = self.num1
        var2 = self.num2
        while True:
            time.sleep(0.3)
            if var2 == 0:
                if var1 < 0:
                    var1 = var1 * (-1)
                print("O mdc({},{}) é {}".format(self.num1,self.num2,var1))
                break
            else:
                resto = var1%var2
                var1 = var2
                var2 = resto
                print("mdc({},{})...".format(var1, var2))
