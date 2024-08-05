""" Calcule el IMC de una persona dado su peso y estatura posteriormente lo clasificaremos de acuerdo a la siguiente tabla
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
 
Edad = input("ingrese su edad")
while not Edad.isdigit():
     print("INVALIDO: favor ingresar edad con caracteres numericos")
     Edad = input("ingrese su edad")
if(Edad < 18):
        print("Usted es menor de edad")
else:
        print("Usted es mayor de edad")

#captura de informacion relevante a IMC
while True:
     peso = float(input("ingrese el peso en Kilogrsamos(kg)"))
     try:
          peso = int(float(input("ingrese su peso")))
          break
     except ValueError:
          print("INVALIDO: favor de ingresar su peso con caracteres numericos")
     
while True:
     estatura = float(input("ingrese su estatura en metros (m)"))
     try:
          estatura = int(float(input("ingrese su estatura en metros (m)")))
          break
     except ValueError:
          print("INVALIDO: favor ingresar su estatura con caracteres numericos")

#determinacion de IMC
IMC = peso / (estatura * estatura)
def IMC(peso, estatura):
    return peso / (estatura * estatura)

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


print(Nombre+", su IMC es"+IMC+", usted "+clasificacionIMC)



