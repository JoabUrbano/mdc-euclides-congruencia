import time

class Calcular:
    """
    Construtor da classe

    :param num1: int
    :param num2: int
    """
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    """
    Calcular a congruência entre dois números
    """
    def congruencia(self):
        resto = self.num1%self.num2
        print("{} é congruente a {}(mod {})".format(self.num1, resto, self.num2))

    """
    Calcular o mdc com algoritimo de euclides, incluindo de números negativos
    """
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
