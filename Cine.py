Edad = int(input("Ingrese su edad: "))
if Edad <= 0:
    print("Edad inválida")
elif Edad < 5:
    print("Entrada gratuita")
elif Edad >= 5 and Edad <= 11:
    print("Entrada cuesta 5000 pesos")
elif Edad >= 12 and Edad <= 59:
    print("Entrada cuesta 8000 pesos")
else:
    print("Entrada cuesta 4000 pesos por descuento a personas mayores")