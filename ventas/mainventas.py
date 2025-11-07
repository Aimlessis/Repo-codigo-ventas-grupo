ventas = []

print("====REGISTRO DE VENTAS==== \n")

numero_ventas = int(input("Ingrese el numero de ventas que quiera registrar: \n"))

for i in range(numero_ventas):
    print(f'venta {i +1}')
    producto = input("ingrese el nombre del producto: \n")
    precio = float(input("ingrese el precio: \n"))

    ventas.append({"Producto": producto, "Precio": precio})

precio_total = 0
for venta in ventas:
    print(f"venta \n")
    print(f"producto: {venta['Producto']} \n")
    print(f"precio: {venta['Precio']} \n")

    precio_total += venta['Precio']


print(f"el total es {precio_total}")