# Supermercado AhorroMax — Descuentos y envío

producto = 2000
cantidad = int(input("Ingrese la cantidad de productos: "))

# Calcular subtotal
subtotal = producto * cantidad

# Determinar el descuento según la cantidad
if cantidad >= 30:
    descuento = 0.15
elif cantidad >= 10:
    descuento = 0.05
else:
    descuento = 0

# Calcular total con descuento
total_con_descuento = subtotal * (1 - descuento)

# Aplicar envío si corresponde
if total_con_descuento < 50000:
    total_final = total_con_descuento + 5000
else:
    total_final = total_con_descuento

# Mostrar resultados
print(f"Subtotal: {subtotal:,.0f}")
print(f"Descuento aplicado: {descuento * 100:,.0f}%")
print(f"Total con descuento: {total_con_descuento:,.0f}")
if total_con_descuento < 50000:
    print("Se agregó envío de $5,000")
print(f"Total final a pagar: {total_final:,.0f}")
