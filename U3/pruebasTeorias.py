colores = ["rojo", "verde"]

print (colores)

for color in colores:
    color = "negro"
    
print(colores)

for i in range(0, len(colores) -1):
    colores[i] = "negro"
    
print(colores)