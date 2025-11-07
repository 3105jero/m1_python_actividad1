hora=2000
multa=5000
tiempo=int(input("Ingrese el tiempo que estuvo parqueado en horas: "))

if tiempo>=0 and tiempo<=5:
    tarifa=tiempo*hora
    print(f"El total a pagar es: {tarifa} pesos")
elif tiempo>5:
    tarifa=tiempo*hora+multa
    print(f"El total a pagar es: {tarifa} pesos")
else:
    print("numero no valido")