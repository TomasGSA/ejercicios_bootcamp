class vehiculo:
    color = ""
    ruedas = 0
    puertas = 0
class coche(vehiculo):
    velociad = 0
    cilindrada = 0.0
class MercedezAMG(coche):
    color = "plateado"
    ruedas = 4
    puertas = 4
    velociad = 250
    cilindrada = 2.6

mercedez = MercedezAMG

print(f'Color es: {mercedez.color}')
print(f'tiene {mercedez.ruedas} ruedas')
print(f'tiene {mercedez.puertas} puertas')
print(f'Velocidad maxima: {mercedez.velociad}')
print(f'Cilindrada de: {mercedez.cilindrada}')


-------------------------------------------------------------------------------------------------------------------------------

class alumno:
    nota = 0.0
    nombre = ""
            
al = alumno
al.nombre = "Tomas Guerrero"
al.nota = 10.0

if al.nota >= 5.0:
        print(f"el alumno {al.nombre} tiene una nota {al.nota} y esta aprobado")
else:
        print(f"El alumno {al.nombre} tiene una nota {al.nota} y esta reprobado")



