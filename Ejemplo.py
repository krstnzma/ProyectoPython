""" Calcule el IMC de una persona dado su peso y estatura lo clasificaremos de acuerdo a la siguiente tabla
------
IMC          Clasificacion
  < 18.49       = bajo peso
18.50 - 24.99   = peso normal
25.00 - 29.99   = sobrepeso
30.00 - 34.99   = obesidad leve
35.00 - 39.99   = obesidad media
Mayor - 40.0    = obesidad mórbida

IMC = peso / (estatura * estatua)
"""
#captura de informacion no relevante a IMC
print("hola, usted esta utilizando la calculadora IMC")
print()

while True:
     Nombre = input("ingrese su Nombre: ")

     try:
          Nombre.isalpha
          break
     except Nombre.isalnum:
          print("INVALIDO: favor de ingresar caracteres alfabteicos")
print("Hola"+Nombre+"! Bienvenidos, ")
 
while True:
     Edad = float(input("ingrese su edad: "))
     try:
          Edad = int(Edad)
          break
     except ValueError:
          print("INVALIDO: favor de ingresar su edad con caracteres numericos")


#captura de informacion relevante a IMC
while True:
     peso = float(input("ingrese el peso en Kilogrsamos(kg): "))
     try:
          peso = int(peso)
          break
     except ValueError:
          print("INVALIDO: favor de ingresar su peso con caracteres numericos")

estatura = float(input("ingrese su estatura en metros (m): "))

#determinacion de IMC

def calcularIMC(p, a):
     return p / (a * a)

def clasificacionIMC(IMC):
    if IMC < 18.49:
        return "esta bajo peso"
    elif 18.5 <= IMC <= 24.99:
        return "esta normal"
    elif 25.0 <= IMC <= 29.99:
        return "esta sobrepeso"
    elif 30.0 <= IMC <= 34.99:
        return " padece de obesidad leve"
    elif 35.0 <= IMC <= 39.99:
        return "padece de obesidad media"
    elif IMC >= 40:
        return "padece de obesidad morbida"

print(Nombre+", usted "+clasificacionIMC(calcularIMC(peso, estatura)))




