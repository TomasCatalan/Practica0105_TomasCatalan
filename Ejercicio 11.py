x = float(input("introduzca saldo en cuenta"))
y = float(0.04)
ba1 = round(x * (1 + y), 2)
ba2 = round(ba1 * (1 + y), 2)
ba3 = round(ba2 * (1 + y), 2)

print("El resultado del balance de año 1 es", ba1, "euros", end="\n")
print("El resultado del balance de año 2 es", ba2, "euros", end="\n")
print("El resultado del balance de año 3 es", ba3, "euros", end="\n")