# Fucion para saber si un año es bisiesto


#ano = 365
#bisiesto = 366

def Calcular():
    ano = int(input("indique año:  "))
    if ano % 4 != 0:
        print(ano, "no es bisiesto")
    elif ano % 4 == 0 and ano % 100 != 0:
        print(ano, "es bisiesto") 
    elif ano % 4 == 0  and ano % 100 == 0 and ano % 400 != 0:
        print(ano, "no es bisiesto")
    elif ano % 4 == 0 and ano % 100 == 0 and ano & 400 == 0:
        print(ano, "es bisiesto")


Calcular()
