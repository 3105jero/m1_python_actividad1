menu=12000
bebida=3000 
preguntac=input("quieres el menu?")
pregunta=input("quieres una bebida?si/no").lower()


if preguntac== "si" and pregunta=="si":
    precio=menu+bebida
    print("el precio total es:",precio, "con iva incluido(8%) quedaria",precio*1.08)
elif preguntac=="no" and pregunta=="si":
    precio=bebida
    print("el precio total es:",precio, "con iva incluido(8%) quedaria",precio*1.08)
elif preguntac=="si" and pregunta=="no":
        precio=menu
        print("el precio total es:",precio, "con iva incluido(8%) quedaria",precio*1.08)
else:
        print("el precio total es: 0")



