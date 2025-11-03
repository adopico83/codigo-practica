productos = []
producto = input("Producto: ")

while producto != "fin":
    productos.append(producto)
    producto = input("Producto: ")

for i in range(len(productos)):
    print(i + 1, ".", productos[i])

