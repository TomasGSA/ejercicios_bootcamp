#Ejercicio de calcular peso corporal 



print ("*** Hola ****")
print ("")

peso = int(input("Indique su peso en Kg --> "))
estatura = float(input("Indique su estatura en metros --> "))

IMC = peso / (estatura * estatura)


print (f'Tu indice de masa corporal es {round(IMC, 2)}')