Pan=300
cantidad=int(input("Ingrese la cantidad de panes que desea comprar: "))
valor_total=Pan*cantidad
if cantidad>=20 and cantidad<50:
    valor_total=valor_total*0.9
    print(valor_total)  
elif cantidad>=50:
    valor_total=valor_total*0.8
    print(valor_total)
elif cantidad <0:
    print("valor invalido")
else:
    cantidad>0 and cantidad<20
    valor_total=Pan*cantidad
    print(valor_total)