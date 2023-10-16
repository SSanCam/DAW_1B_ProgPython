"""1.5 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, 
sino que se imprime desde dentro de la función."""

def precio_final() :
    
    precio_articulo = float(input("Cuanto cuesta el articulo?: "))
    iva = float(input("Que porcentaje de IVA debe aplicarse?: "))
    iva_aplicar = (iva / 100) * precio_articulo
    importe_total = precio_articulo + iva_aplicar

    return print(f"Precio de articulo: {precio_articulo}\nIVA a aplicar: {iva_aplicar}\nEl precio final es de: {importe_total} €.") 

print(precio_final())