nota1=float(input("ingrese la primera nota: "))
nota2=float(input("ingrese la segunda nota: "))
calculo=nota1*0.7+nota2*0.3
if calculo>=3.0:
    print("aprobado")
elif calculo>=2.0 and calculo<3.0:
    print("revision")
else:
    print("reprobado")