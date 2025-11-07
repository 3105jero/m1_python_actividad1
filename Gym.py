Dias = int(input("Ingrese la cantidad de días que vino a entrenar en la semana: "))
if Dias < 0:
    print("Número de días inválido")
elif Dias == 0 or Dias == 1:
    print("No aflojes,puedes mejorar")
elif Dias == 2 or Dias == 3:
    print("bien,pero puedes esforzarte más")
elif Dias >= 4 and Dias <= 7:
    print("excelente, eres un ejemplo a seguir")
else:
    print("No existen más días de la semana")
