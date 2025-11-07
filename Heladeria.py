chocolate = 4000
vainilla = 3500
toppings = 1000

print("Bienvenido a la Heladería")
print("Sabores disponibles:")
print(f"Chocolate: {chocolate} pesos")
print(f"Vainilla: {vainilla} pesos")
print(f"Toppings: {toppings} pesos")
sabor = input("Ingrese el sabor que desea (chocolate/vainilla): ").lower()
cantidad = int(input("Ingrese la cantidad de helados que desea comprar: "))
cantidadt=int(input("Ingrese la cantidad de toppings que desea tener: "))


if cantidadt!=0:
    toppings=cantidadt*toppings



if sabor == "chocolate":
    total = chocolate * cantidad + toppings
elif sabor == "vainilla":
    total = vainilla * cantidad + toppings
else:
    total = 0


print(f"El total a pagar es: {total} pesos")