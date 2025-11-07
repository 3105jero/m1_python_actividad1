libro=25000
cliente=input("que eres? estudiante/cliente normal: ").lower()
ticket=input("tiene ticket de descuento? si/no: ").lower()

if cliente=="estudiante":
    descuento=0.85
    total=(libro*descuento)
    print(f"el total a pagar es de: {total} pesos")

elif cliente=="cliente normal" and ticket=="si":
    descuento=0.9
    total=(libro*descuento)
    print(f"el total a pagar es de: {total} pesos")

elif cliente=="estudiante" and ticket=="si":
    descuento=0.85
    descuenton=descuento*0.9
    total=(libro*descuenton)
    print(f"el total a pagar es de: {total} pesos")

else:

    total=libro

    print(f"el total a pagar es de: {total} pesos")

