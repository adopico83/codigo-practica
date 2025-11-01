importe = float(input("Importe de la compra: "))

if importe < 50:
    descuento = 0

elif importe >= 50 and importe <= 100:

     descuento = (importe * 0.10)


elif importe > 100:

    descuento = (importe * 0.20)

precio_final = importe - descuento
print("Precio final a pagar:", precio_final, "€")