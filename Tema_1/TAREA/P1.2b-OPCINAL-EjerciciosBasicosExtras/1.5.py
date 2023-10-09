"""Ejercicios 1.5 al 1.10
Usar tipos de datos float y mostrar con 2 posiciones decimales."""

"""EJ 2.5
Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo."""

precio_articulo = float(input("Cuanto cuesta el articulo?: "))
iva = float(input("Que porcentaje de IVA debe aplicarse?: "))
iva_aplicar = (iva / 100) * precio_articulo
importe_total = precio_articulo + iva_aplicar
importe_total_formateado = "{:.2f}€".format(importe_total)

print(f"El precio final es de: {importe_total_formateado}.")

"""EJ 2.6
Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%)."""

importe_bruto = float(input("Cual es el precio final del articulo?: "))
importe_siniva = importe_bruto - (importe_bruto * 0.1)
print(f"El articulo tiene un precio final de {importe_bruto:.2f}€ y tiene aplicado un IVA del 10%, su precio sin IVA es de: {importe_siniva:.2f}€.")

"""EJ 2.7
Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma."""
cantidad_numeros = 3
cantidad_total = 0.0

while cantidad_numeros != 0 :
    cantidad_total += float(input("Introduce un numero: "))
    cantidad_numeros -= 1

media_final = cantidad_total / 3

print(f"La suma total es de {cantidad_total:.2f}, y la media es de: {media_final:.2f}")

"""EL 2.8
Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes."""
numero1 = int(input("Introduce un numero entero: "))
numero2 = int(input("Introduce otro numero entero: "))

print(f"La suma de {numero1} + {numero2} hace un total de: {numero1 + numero2:.2f}")

"""EJ 2.9
¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo."""

print("{:.2f}".format(float(input("Introduce un numero: "))+float(input("Introduce un numero: "))+float(input("Introduce un numero: "))))

"""Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética.
"""
formula = (((2+3)/2.5)**2)
formula_formateada = "{:.2f}".format(formula)
