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



