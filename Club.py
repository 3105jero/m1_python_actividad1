
edad = int(input("Ingrese su edad: "))
documento = input("¿Tiene documento? (sí/no): ").lower()


if edad < 18:
    print("Entrada denegada")
elif edad >= 18 and documento == "sí":
    print(" Bienvenido al Club ")
else:
    print("Debe presentar documento")
