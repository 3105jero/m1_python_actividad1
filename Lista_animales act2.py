print("1.crear un nuevo animal")
print("2.mostrar los animales")
print("3.borrar un animal por id(posicion de lista)")
print("4.borrar animal por nombre")
print("5.borrar todos los animales")
print("6.listar animal por id(posicion de lista)")


follow=True
numero=int(input("ingrese una opcion: "))
animals=[]

while follow:
    if numero==1:
        nombre_animal=input("ingrese el nombre del animal: ").lower()
        animals.append({"nombre":nombre_animal})
    elif numero==2:
        print(animals)
    elif numero==3:
        id_borrar=int(input("ingrese el id del animal a borrar: "))
        if 0 <= id_borrar < len(animals):
            animals.pop(id_borrar)
    elif numero==4:
        nombre_borrar=input("ingrese el nombre del animal a borrar: ").lower()
        for animal in animals:
            if animal["nombre"]==nombre_borrar:
                animals.remove(animal)
    elif numero==5:
        animals.clear()
    elif numero==6:
        id_listar=int(input("ingrese el id del animal a listar: "))
        if 0 <= id_listar < len(animals):
            print(animals[id_listar])
    else:
        follow=False
    numero=int(input("ingrese una opcion: "))

