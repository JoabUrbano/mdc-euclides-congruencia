#Feito por Joab Urbano
from Calcular import *
print("Digite 1 para congruencia e 2 para mdc com euclides")
print("")
while True:
    op = input("Digite a opção desejada: ")
    print("")
    try:
        x = int(op)
        if int(op) == 1:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            cal = Calcular(num1, num2)
            cal.congruencia()

        elif int(op) == 2:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            cal = Calcular(num1, num2)
            cal.mdc_euclides()

        else:
            print("Opção invalida.")

        op  = input("Deseja continuar? (N para cancelar): ")
        if op.lower() == "n":
            break
        else:
            print("")
    except:
        print("Opção invalida.")
        print("")
